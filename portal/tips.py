from typing import List

import pymongo

from portal.database import mongo


def get_all_tips():
    """Fetch all tips from the 'tips' collection in MongoDB.

    This function queries the 'tips' collection to retrieve all documents
    contained within it. The results are sorted by the '_id' field in
    descending order, which effectively returns the most recently created
    tips first, as MongoDB ObjectIds are partially based on a timestamp.

    Returns:
        pymongo.cursor.Cursor
    """

    tips = mongo.db.tips.find().sort({'_id': -1})
    return tips


def get_tips_by_tag(tag: str) -> pymongo.cursor.Cursor:
    """Find all tips that match a given tag, sorted by creation date.

    This function queries the 'tips' collection for documents where the
    'tags' field (expected to be an array of strings) contains the
    specified tag. The results are sorted by the '_id' field in descending
    order, ensuring that the most recently created tips are returned first.

    Args:
        tag: str
            The specific tag to search for within the tips' tags.

    Returns:
        pymongo.cursor.Cursor
    """

    tips = mongo.db.tips.find({'tags': tag}).sort({'_id': -1})
    return tips


def get_unique_tags() -> List[str]:
    """Retrieve a sorted list of all unique tags directly from MongoDB.

    This function uses the MongoDB Aggregation Framework to efficiently find
    and sort all unique tags. The pipeline unwinds the 'tags' array, groups
    the tags to get unique values, sorts them, and finally groups them
    back into a single list. This approach is more performant for large
    datasets as all heavy lifting is done on the database server.

    Returns:
        List[str]
    """

    pipeline = [
        {'$unwind': '$tags'},
        {'$group': {'_id': '$tags'}},
        {'$sort': {'_id': 1}},
        {'$group': {'_id': None, 'unique_tags': {'$push': '$_id'}}},
    ]

    result = list(mongo.db.tips.aggregate(pipeline))
    return result[0].get('unique_tags', []) if result else []
