from authz import ma
from authz.model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        '''
            this class is for Marshmalow.
            Fetch mode vie SQLAlchemy
            It helps for serialization and deserialization
            It helps for Validation
        '''
        model = User

    id = ma.auto_field(dump_only=True)  # dump_only means Only readable
    username = ma.auto_field()
    password = ma.auto_field(load_only=True)  # Only is writable
    role = ma.auto_field()
    register_at = ma.auto_field(dump_only=True)
    last_active_at = ma.auto_field(dump_only=True)
    last_failed_at = ma.auto_field(dump_only=True)
    status = ma.auto_field()
