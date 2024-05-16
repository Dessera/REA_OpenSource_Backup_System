from enum import IntEnum
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class UserDepartment(IntEnum):
    PROJECT_DEPARTMENT = 1
    SECRETARY_DEPARTMENT = 2
    PRACTICE_DEPARTMENT = 3
    PUBLICITY_DEPARTMENT = 4


class UserOrm(Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=50, unique=True, null=False)
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    department = fields.IntEnumField(UserDepartment)
    student_id = fields.CharField(max_length=8, unique=True, null=False)

    def __str__(self):
        return self.username

    class Meta:
        table = "users"

    class PydanticMeta:
        exclude = ["password"]


User = pydantic_model_creator(UserOrm, name="User")
