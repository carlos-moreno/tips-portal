from __future__ import annotations
from portal.database import mongo
from datetime import datetime
import pymongo

def get_all_tips():
    """Return all tips
    """
    tips = mongo.db.tips.find()
    return tips


def get_tips_by_tag(tag: str) -> dict:
    """Return one post by tag
    """
    tips = mongo.db.tips.find({"tags": tag})
    return tips

def get_unique_tags() -> dict:
    """Return one post by tag
    """
    return sorted(mongo.db.tips.distinct("tags"))