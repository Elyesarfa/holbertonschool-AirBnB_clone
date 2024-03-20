#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            format = "%Y-%m-%dT%H:%M:%S.%f"
            try:
                self.id = kwargs["id"]
                x = datetime.strptime(kwargs["created_at"], format)
                y = datetime.strptime(kwargs["updated_at"], format)
                self.created_at = x
                self.updated_at = y
            except KeyError:
                pass

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
