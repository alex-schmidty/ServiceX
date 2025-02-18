from flask import current_app
from servicex_app.models import UserModel


def check_user_exists(sub):
    return UserModel.find_by_sub(sub)


def add_user(sub, email, name, institution, refresh_token):
    new_user = UserModel(
        sub=sub,
        email=email,
        name=name,
        institution=institution,
        refresh_token=refresh_token)

    if new_user.email == current_app.config.get('JWT_ADMIN'):
        new_user.admin = True
    if refresh_token:
        new_user.pending = False
    else:
        new_user.pending = True
    try:
        if not check_user_exists(new_user.sub):
            new_user.save_to_db()
    except Exception as ex:
        print(str(ex))


def list_users() -> None:
    users = UserModel.query.all()
    print("Sub, Email, Name, Institution, Pending?")
    for user in users:
        print(", ".join([user.sub, user.email, user.name, user.institution,
                         "Pending" if user.pending else "Approved"]))


def approve_user(sub: str) -> None:
    user = UserModel.find_by_sub(sub)
    if user and user.pending:
        user.pending = False
        user.save_to_db()
        print(f"User {sub} approved")
    elif user and not user.pending:
        print(f"User {sub} already approved")
    else:
        print(f"User {sub} not found")
