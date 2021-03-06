from flask import Blueprint, session, request, redirect, url_for, render_template
from . import db
from .auth import userLoggedIn,userType

client = Blueprint('client',__name__)

@client.route('/viewclientprofile', methods= ['POST'])
def viewprofile():
    if not(userLoggedIn() and userType('client')):
        return
    dbCursor = db.cursor()
    sql = "SELECT client_name, client_ph, client_email, client_aadhar, \
    client_PAN, client_DOB FROM client_database WHERE client_ID=%s"
    val = (session['id'])
    dbCursor.execute(sql, val)
    res = dbCursor.fetchone()
    dbCursor.close()
    return res


@client.route('/viewallpolicies', methods= ['POST'])
def viewallpolicies():
    if not(userLoggedIn() and userType('client')):
        return
    dbCursor = db.cursor()
    sql = "SELECT policy_name, ins_type, min_coverage, premium, eligibility_cond, \
    terms_conditions FROM policy_database"
    dbCursor.execute(sql)
    res = dbCursor.fetchall()
    dbCursor.close()
    return res

@client.route('/viewinsurances', methods= ['POST'])
def viewinsurances():
    if not(userLoggedIn() and userType('client')):
        return
    dbCursor = db.cursor()
    sql = "SELECT * FROM insurance_database WHERE client_ID = %s"
    val = (session['id'])
    dbCursor.execute(sql, val)
    res = dbCursor.fetchall()
    dbCursor.close()
    return res

@client.route('/boughtInsurance', methods=['POST'])
def boughtInsurance():
	if not(userLoggedIn() and userType('client')):
		return
		
