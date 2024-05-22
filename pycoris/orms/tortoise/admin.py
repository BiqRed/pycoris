from enum import Enum

try:
    from tortoise import Model, fields
except ImportError:
    raise ImportError(
        'TortoiseORM is not installed. '
        'Please install it with: '
        'pip install pycoris[tortoise-orm]'
    )


class AdminUser(Model):
    class Meta:
        table = 'pycoris_admins'
        table_description = 'Pycoris Admins'

    username = fields.CharField(
        max_length=64,
        unique=True,
        null=False,
        description='Admin username',
    )

    password = fields.CharField(
        max_length=128,
        null=False,
        description='Admin hashed password',
    )

    email = fields.CharField(
        max_length=128,
        unique=True,
        null=True,
        description='Admin email',
    )

    name = fields.CharField(
        max_length=128,
        null=True,
        description='Admin name',
    )

    is_active = fields.BooleanField(
        default=True,
        description='Admin is active',
    )

    is_superuser = fields.BooleanField(
        default=False,
        description='Admin is superuser',
    )

    created_at = fields.DatetimeField(
        auto_now_add=True,
        description='Admin created at',
    )
    last_login_at = fields.DatetimeField(
        null=True,
        description='Admin last login at',
    )

    permissions: fields.ManyToManyRelation['AdminPermission'] = fields.ManyToManyField(
        'pycoris.models.tortoise.admin.AdminPermission',
        related_name='admins',
        description='Admin permissions',
    )

    groups: fields.ManyToManyRelation['AdminGroup'] = fields.ManyToManyField(
        'pycoris.models.tortoise.admin.AdminGroup',
        related_name='admins',
        description='Admin groups',
    )

    logs: fields.ForeignKeyRelation['AdminLog']

    def __str__(self):
        return self.username


class AdminPermission(Model):
    class Meta:
        table = 'pycoris_permissions'
        table_description = 'Pycoris Permissions'

    name = fields.CharField(
        max_length=256,
        unique=True,
        null=False,
        description='Permission name',
    )

    code = fields.CharField(
        max_length=128,
        unique=True,
        null=False,
        description='Permission code',
    )

    type = fields.CharField(
        max_length=256,
        null=True,
        description='Permission type',
    )

    admins: fields.ManyToManyRelation['AdminUser']

    def __str__(self):
        return self.name


class AdminGroup(Model):
    class Meta:
        table = 'pycoris_groups'
        table_description = 'Pycoris Groups'

    name = fields.CharField(
        max_length=256,
        unique=True,
        null=False,
        description='Group name',
    )

    admins: fields.ManyToManyRelation['AdminUser']

    def __str__(self):
        return self.name


class AdminLogType(str, Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
    ACTION = 'action'


class AdminLog(Model):
    class Meta:
        table = 'pycoris_logs'
        table_description = 'Pycoris Admin Logs'

    admin: fields.ForeignKeyRelation['AdminUser'] = fields.ForeignKeyField(
        'pycoris.models.tortoise.admin.AdminUser',
        related_name='logs',
        description='Admin',
    )

    created_at = fields.DatetimeField(
        auto_now_add=True,
        description='Log created at',
    )

    object_id = fields.BigIntField(
        null=True,
        description='Log object id',
    )

    object_name = fields.CharField(
        max_length=256,
        null=True,
        description='Log object name',
    )

    type = fields.CharEnumField(
        enum_type=AdminLogType,
        description='Log type',
    )

    values = fields.JSONField(
        null=True,
        description='Log values',
    )

    def __str__(self):
        return self.type
