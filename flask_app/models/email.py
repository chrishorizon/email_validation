from flask_app.config.mysqlcontroller import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    validation = "email_validation"
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def submit_email(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.validation).query_db(query,data)

    @classmethod
    def get_emails(cls):
        query= "SELECT * FROM emails"
        results = connectToMySQL(cls.validation).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails
    
    # @classmethod
    # def get_one_email(cls):
    #     query = 'SELECT * FROM emails WHERE id = %(id)s'
    #     result = connectToMySQL(cls.validation).query_db(query)
    #     return cls(result[0])

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.validation).query_db(query,data)

    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.validation).query_db(query,email)
        if len(results) > 0:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("")
            is_valid=False
        return is_valid