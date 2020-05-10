#coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """admin login form"""
    account = StringField(
        label="帐号",
        validators=[
            DataRequired("请输入帐号！")
        ],
        description="帐号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入帐号！",
            # "required": "required"
        }
    )
    pwd = StringField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )
