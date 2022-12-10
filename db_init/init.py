import psycopg2

conn = psycopg2.connect(database = "eczane", user = "postgres", password = "Yigit1323?", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute('''create table if not EXISTS adres (
    adres_id int NOT NULL,
    il varchar(14) DEFAULT NULL,
    ilce varchar(16) DEFAULT NULL,
    posta_kodu int DEFAULT NULL,
    PRIMARY KEY (adres_id)
);''')

cur.execute('''create table if not EXISTS eczane (
    eczane_id int NOT NULL,
    eczane_ad varchar(21) NOT NULL,
    adres_id int NOT NULL,
    PRIMARY KEY (eczane_id),
    constraint FK_adres_id2
        foreign key(adres_id)
            references adres(adres_id)
);''')

cur.execute('''create table if not EXISTS eczaci (
    eczaci_id int NOT NULL,
    eczaci_ad_soyad varchar(28) NOT NULL,
    eczane_id int NOT NULL,
    PRIMARY KEY (eczaci_id),
    constraint FK_eczane_id3
            foreign key(eczane_id)
                references eczane (eczane_id)
);''')

cur.execute('''create table if not EXISTS ilac (
    ilac_id int NOT NULL,
    ilac_ad varchar(31) NOT NULL,
    alis_fiyat int NOT NULL,
    satis_fiyat int NOT NULL,
    envanter int NOT NULL,
    eczane_id int NOT NULL,
    PRIMARY KEY (ilac_id),
    constraint FK_eczane_id2
            foreign key(eczane_id)
                references eczane (eczane_id)
);''')

cur.execute('''create table if not EXISTS hasta (
    hasta_tckn varchar(11) NOT NULL,
    hasta_ad_soyad varchar(25) NOT NULL,
    cinsiyet varchar(1) NOT NULL,
    dog_tar date NOT NULL,
    telefon varchar(10) NOT NULL,
    adres_id int NOT NULL,
    ilac_id int NOT NULL,
    PRIMARY KEY (hasta_tckn),
    constraint FK_adres_id4
                foreign key(adres_id)
                    references adres (adres_id),
    constraint FK_ilac_id
            foreign key(ilac_id)
                references ilac (ilac_id)
);''')


cur.execute('''create table if not EXISTS personel (
    per_tckn varchar(11) NOT NULL,
    per_ad_soyad varchar(30) NOT NULL,
    per_tel_no varchar(10) NOT NULL,
    eczane_id int NOT NULL,
    adres_id int NOT NULL,
    PRIMARY KEY (per_tckn),
    constraint FK_adres_id
        foreign key(adres_id)
            references adres (adres_id),
    constraint FK_eczane_id
        foreign key(eczane_id)
            references eczane (eczane_id)
);''')







conn.commit()
conn.close()