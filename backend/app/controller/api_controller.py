from email.mime import base
from random import randint
import time
import logging
import psycopg2
from datetime import date

from flask import Blueprint, request, jsonify

controller = Blueprint('api_controller', __name__, url_prefix='') # template_folders?
logger = logging.getLogger(__name__)

from . import conn


@controller.route('/eczaneadmin/<string:eczaneId>', methods=['get'])
def eczane(eczaneId):
    cur = conn.cursor()
    cur.execute('''select * from eczane Where eczane_id=%s;''', (eczaneId))
    eczaneler = cur.fetchall()
    result = []
    result.append({'eczane_id':'0','eczane_ad':'','adres_id':'0'})
    for eczane in eczaneler:
        result.append({'eczane_id':eczane[0],'eczane_ad':eczane[1],'adres_id':eczane[2]})
    conn.commit()
    print("sdadas")
    print(result)
    return jsonify(result)


@controller.route('/personel', methods=['get'])
def personel():
    cur = conn.cursor()
    cur.execute('''select * from personel;''')
    personeller = cur.fetchall()
    result = []
    result.append({'per_tckn':'','per_ad_soyad':'','per_tel_no':'','eczane_id':'0','adres_id':'0'})
    for personel in personeller:
        result.append({'per_tckn':personel[0],'per_ad_soyad':personel[1],'per_tel_no':personel[2],'eczane_id':personel[3],'adres_id':personel[4]})
    conn.commit()

    return jsonify(result)

@controller.route('/adres/<string:adresId>', methods=['get'])
def adres(adresId):
    cur = conn.cursor()
    cur.execute('''select * from adres where adres_id=%s;''',(adresId))
    adresler = cur.fetchall()
    result = []
    result.append({'adres_id':'0','il':'','ilce':'','posta_kodu':'0'})
    for adres in adresler:
        result.append({'adres_id':adres[0],'il':adres[1],'ilce':adres[2],'posta_kodu':adres[3]})
    conn.commit()

    return jsonify(result)

@controller.route('/eczaci/<string:eczaciId>', methods=['get'])
def eczaci(eczaciId):
    cur = conn.cursor()
    cur.execute('''select * from eczaci where eczane_id=%s;''',(eczaciId))
    eczacilar = cur.fetchall()
    result = []
    result.append({'eczaci_id':'0','eczaci_ad_soyad':'','eczane_id':'0'})
    for eczaci in eczacilar:
        result.append({'eczaci_id':eczaci[0],'eczaci_ad_soyad':eczaci[1],'eczane_id':eczaci[2]})
    conn.commit()

    return jsonify(result)

@controller.route('/ilac', methods=['get'])
def ilac():
    cur = conn.cursor()
    cur.execute('''select * from ilac;''')
    ilaclar = cur.fetchall()
    result = []
    result.append({'ilac_id':'0','ilac_ad':'','alis_fiyat':'0','satis_fiyat':'0','envanter':'0','eczane_id':'0'})
    for ilac in ilaclar:
        result.append({'ilac_id':ilac[0],'ilac_ad':ilac[1],'alis_fiyat':ilac[2],'satis_fiyat':ilac[3],'envanter':ilac[4],'eczane_id':ilac[5]})
    conn.commit()

    return jsonify(result)

@controller.route('/hasta', methods=['get'])
def hasta():
    cur = conn.cursor()
    cur.execute('''select * from hasta;''')
    hastalar = cur.fetchall()
    result = []
    result.append({'hasta_tckn':'','hasta_ad_soyad':'','cinsiyet':'0','dog_tar':'','telefon':'','adres_id':'0','ilac_id':'0'})
    for hasta in hastalar:
        result.append({'hasta_tckn':hasta[0],'hasta_ad_soyad':hasta[1],'cinsiyet':hasta[2],'dog_tar':hasta[3],'telefon':hasta[4],'adres_id':hasta[5],'ilac_id':hasta[6]})
    conn.commit()

    return jsonify(result)





