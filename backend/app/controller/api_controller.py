from . import conn
from email.mime import base
from random import randint
import time
import logging
import psycopg2
from datetime import date

from flask import Blueprint, request, jsonify

controller = Blueprint('api_controller', __name__,
                       url_prefix='')  # template_folders?
logger = logging.getLogger(__name__)


@controller.route('/eczaneadmin/<string:eczaneId>', methods=['get'])
def eczane(eczaneId):
    cur = conn.cursor()
    cur.execute('''select * from eczane Where eczane_id=%s;''', (eczaneId,))
    eczaneler = cur.fetchall()
    result = []
    result.append({'eczane_id': '0', 'eczane_ad': '', 'adres_id': '0'})
    for eczane in eczaneler:
        result.append(
            {'eczane_id': eczane[0], 'eczane_ad': eczane[1], 'adres_id': eczane[2]})
    conn.commit()
    return jsonify(result)


@controller.route('/personel/<string:eczaneId>', methods=['get'])
def personel(eczaneId):
    cur = conn.cursor()
    cur.execute('''select * from personel, eczane where eczane.eczane_id = %s and eczane.eczane_id=personel.eczane_id;''', (eczaneId,))
    personeller = cur.fetchall()
    result = []
    result.append({'per_tckn': '', 'per_ad_soyad': '',
                  'per_tel_no': '', 'eczane_id': '0', 'adres_id': '0', 'eczane_id': '0','adres_ad': '0', 'adres_id': '0'})
    for personel in personeller:
        result.append({'per_tckn': personel[0], 'per_ad_soyad': personel[1],
                  'per_tel_no': personel[2], 'eczane_id': personel[3], 'adres_id': personel[4], 'eczane_id': personel[5],'adres_ad': personel[6], 'adres_id': personel[7]})
    conn.commit()

    return jsonify(result)


@controller.route('/adres/<string:adresId>', methods=['get'])
def adres(adresId):
    cur = conn.cursor()
    cur.execute('''select * from adres where adres_id=%s;''', (adresId,))
    adresler = cur.fetchall()
    result = []
    result.append({'adres_id': '0', 'il': '', 'ilce': '', 'posta_kodu': '0'})
    for adres in adresler:
        result.append(
            {'adres_id': adres[0], 'il': adres[1], 'ilce': adres[2], 'posta_kodu': adres[3]})
    conn.commit()

    return jsonify(result)


@controller.route('/eczaci/<string:eczaciId>', methods=['get'])
def eczaci(eczaciId):
    cur = conn.cursor()
    cur.execute('''select * from eczaci where eczane_id=%s;''', (eczaciId,))
    eczacilar = cur.fetchall()
    result = []
    result.append({'eczaci_id': '0', 'eczaci_ad_soyad': '', 'eczane_id': '0'})
    for eczaci in eczacilar:
        result.append(
            {'eczaci_id': eczaci[0], 'eczaci_ad_soyad': eczaci[1], 'eczane_id': eczaci[2]})
    conn.commit()

    return jsonify(result)


@controller.route('/ilac/<string:eczaneId>', methods=['get'])
def ilac(eczaneId):
    cur = conn.cursor()
    cur.execute(
        '''select * from ilac where eczane_id=%s order by ilac_id asc;''', (eczaneId,))
    ilaclar = cur.fetchall()
    result = []
    result.append({'ilac_id':'0','ilac_ad':'','alis_fiyat':'0','satis_fiyat':'0','envanter':'0','eczane_id':'0'})
    for ilac in ilaclar:
        result.append({'ilac_id': ilac[0], 'ilac_ad': ilac[1], 'alis_fiyat': ilac[2],
                      'satis_fiyat': ilac[3], 'envanter': ilac[4], 'eczane_id': ilac[5]})
    conn.commit()

    return jsonify(result)


@controller.route('/tekilac/<string:ilacId>', methods=['get'])
def tekilac(ilacId):
    cur = conn.cursor()
    cur.execute(
        '''select * from ilac where ilac_id=%s;''', (ilacId,))
    ilaclar = cur.fetchall()
    result = []
    result.append({'ilac_id':'0','ilac_ad':'','alis_fiyat':'0','satis_fiyat':'0','envanter':'0','eczane_id':'0'})
    for ilac in ilaclar:
        result.append({'ilac_id': ilac[0], 'ilac_ad': ilac[1], 'alis_fiyat': ilac[2],
                      'satis_fiyat': ilac[3], 'envanter': ilac[4], 'eczane_id': ilac[5]})
    conn.commit()

    return jsonify(result)


@controller.route('/removeMedicine', methods=['post'])
def removeMedicine():
    if request.json is not None:
        eczaneId = request.json['eczane_id']
        ilacId = request.json['ilac_id']
        ilac=tekilac(ilacId)
        if ilac.json is not None:
            print(ilac.json[1])
            envanter = ilac.json[1]['envanter']
        else:
            return 'ilac_id must be defined', 400
    else:
        return 'eczane_id must be defined', 400

    cur = conn.cursor()

    try:
        print(envanter)
        if(envanter-1 <= 0 ):
            deleteQuery='''DELETE FROM ilac WHERE ilac_id=%s; '''
            cur.execute(deleteQuery,(ilacId,))

        else:
            updateQuery = ''' update ilac
            set envanter = envanter - 1 
            where ilac_id = %s and ilac.eczane_id = %s'''
            cur.execute(updateQuery, (ilacId, eczaneId,))
    except:
        return jsonify({"message": "bir hata olustu"})
    conn.commit()

    return jsonify({"message": "basariyla silindi"})

@controller.route('/removePer', methods=['post'])
def removePer():
    if request.json is not None:
        pertckn = request.json['per_tckn']
    else:
        return 'car_id must be defined', 400

    cur = conn.cursor()

    try:
        cur.execute(''' DELETE FROM personel WHERE per_tckn=%s;''',(pertckn,))
        
    except:
        return jsonify({"message": "bir hata olustu"})
    conn.commit()

    return jsonify({"message": "basariyla silindi"})


@controller.route('/addMedicine', methods=['post'])
def addMedicine():
    print("addMEd içi")
    if request.json is not None:
        data = request.json
        print(data)
        alis_fiyat = data['alis_fiyat']
        eczane_id = data['eczane_id']
        envanter = data['envanter']
        ilac_id = data['ilac_id']
        ilac_ad = data['ilac_ad']
        satis_fiyat = data['satis_fiyat']
    else:
        return 'id must be defined', 400
    cur = conn.cursor()

    try:
        addQuery = ''' INSERT INTO ilac (ilac_id, ilac_ad, alis_fiyat, satis_fiyat, envanter, eczane_id)
        VALUES (%s, %s, %s, %s, %s, %s);'''
        cur.execute(addQuery, (ilac_id, ilac_ad, alis_fiyat,
                    satis_fiyat, envanter, eczane_id,))
    except:
        return jsonify({"message": "bir hata olustu"})
    conn.commit()

    return jsonify({"message": "basariyla silindi"})



@controller.route('/hasta/<string:tcNum>', methods=['get'])
def hasta(tcNum):
    cur = conn.cursor()
    cur.execute('''select * from hasta where hasta_tckn=%s;''', (tcNum,))
    hastalar = cur.fetchall()
    result = []
    result.append({'hasta_tckn': '', 'hasta_ad_soyad': '', 'cinsiyet': '0',
                  'dog_tar': '', 'telefon': '', 'adres_id': '0', 'ilac_id': '0'})
    for hasta in hastalar:
        result.append({'hasta_tckn': hasta[0], 'hasta_ad_soyad': hasta[1], 'cinsiyet': hasta[2],
                      'dog_tar': hasta[3], 'telefon': hasta[4], 'adres_id': hasta[5], 'ilac_id': hasta[6]})
    conn.commit()

    return jsonify(result)

@controller.route('/hasta_eczane/<string:tcNum>', methods=['get'])
def hasta_eczane(tcNum):
    cur = conn.cursor()
    cur.execute('''select eczane_ad, adres.il from hasta, ilac, eczane, adres where hasta.hasta_tckn = %s 
    and hasta.ilac_id = ilac.ilac_id and eczane.eczane_id = ilac.eczane_id 
    and eczane.adres_id=adres.adres_id ;''', (tcNum,))
    hastalar_eczane = cur.fetchall()
    result = []
    result.append({'eczane_ad': '', 'il': ''})
    for hasta_eczane in hastalar_eczane:
        result.append({'eczane_ad': hasta_eczane[0], 'il': hasta_eczane[1]})
    conn.commit()

    return jsonify(result)
