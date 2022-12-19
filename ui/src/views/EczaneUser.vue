<template>
    <div style='heigth : 100vh'>
        <div style="myCars">
            <h3>
                Profile:
            </h3>
            <p>
                Tc Kimlik Numarası: {{ tcNum }}
            </p>
            <p>
                Hasta Isim ve Soyisim : {{ hasta_ad_soyad }}
            </p>
            <p>
                Cinsiyet : {{ cinsiyet }}
            </p>
            <p>
                Doğum Tarihi : {{ dog_tar }}
            </p>
            <p>
                Adres : {{ adres }}
            </p>
            <p>
                Telefon Numarası : {{ telefon }}
            </p>
            <p>
                Bulunan Eczane : {{ eczane_ad }}
                {{ il }}
            </p>
            <p>
                Hastanın ilacı ve fiyatı: {{ tekilac }} {{ ilacfiyati }} tl

            </p>
        </div>
        <div>

            <table border="1" style="background-color: #656569;">
                <thead>
                    <tr>
                        <th>Eczanede bulunan ilaçlar</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in ilaclar" :key="item.ilac_id">
                        <td>{{ item.ilac_ad }}</td>
                        <td><button class='button-black' @click="makeActive(item.ilac_id)">
                                Aktif ilaç olarak seç
                            </button></td>
                    </tr>
                </tbody>
                <button class='button-black' @click="$router.go(-1)">Geri Dön</button>
            </table>
        </div>
    </div>
</template>

<script>
import router from '@/router';

export default {
    name: 'EczaneUser',
    components: {
    },
    data() {
        return {
            tcNum: null,
            ev_adres_id: null,
            cinsiyet: "",
            dog_tar: "",
            hasta_ad_soyad: "",
            ilac_id: "",
            telefon: "",
            adres: "",
            eczaneId: "",
            ilaclar: [],
            eczane_ad: "",
            il: "",
            tekilac: "",
            ilacfiyati: ""
        }
    },
    created() {
        const pageInfo = this.$router.currentRoute.value;
        this.tcNum = pageInfo.params.tcNum;
        const url1 = 'http://127.0.0.1:5000/hasta/' + this.tcNum;
        fetch(url1)
            .then(async response => {
                const data = await response.json();
                if (!response.ok) {
                    const error = (data && data.message) || response.statusText;
                    return Promise.reject(error);
                }
                console.log(data)
                this.hasta_ad_soyad = data[1].hasta_ad_soyad;
                this.telefon = data[1].telefon;
                this.adres = data[1].adres;
                this.dog_tar = data[1].dog_tar;
                this.cinsiyet = data[1].cinsiyet;
                this.ev_adres_id = data[1].adres_id;
                this.ilac_id = data[1].ilac_id;

                const url2 = 'http://127.0.0.1:5000/adres/' + this.ev_adres_id;
                console.log(url2);
                fetch(url2)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        this.adres = data[1].il + " " + data[1].ilce + " " + data[1].posta_kodu;
                    })
                    .catch(error => {
                        this.errorMessage = error;
                        console.error("There was an error!", error);
                    });
                const url7 = 'http://127.0.0.1:5000/hasta_eczane/' + this.tcNum;
                console.log(url7);
                fetch(url7)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        this.eczane_ad = data[1].eczane_ad;
                        this.il = data[1].il;
                    })
                    .catch(error => {
                        this.errorMessage = error;
                        console.error("There was an error!", error);
                    });

                const url3 = 'http://127.0.0.1:5000/tekilac/' + this.ilac_id;
                console.log(url3);
                fetch(url3)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        this.tekilac = data[1].ilac_ad;
                        this.ilacfiyati = data[1].satis_fiyat;

                        console.log(data)
                        this.eczaneId = data[1].eczane_id
                        const url4 = 'http://127.0.0.1:5000/ilac/' + this.eczaneId;
                        fetch(url4)
                            .then(async response => {
                                const data = await response.json();
                                if (!response.ok) {
                                    const error = (data && data.message) || response.statusText;
                                    return Promise.reject(error);
                                }
                                data.forEach(element => {
                                    if (element['ilac_id'] != 0) {
                                        this.ilaclar.push(element)
                                    }
                                    console.log(element)
                                });
                            })
                            .catch(error => {
                                this.errorMessage = error;
                                console.error("There was an error!", error);
                            });
                    })
                    .catch(error => {
                        this.errorMessage = error;
                        console.error("There was an error!", error);
                    });
            })
            .catch(error => {
                this.errorMessage = error;
                console.error("There was an error!", error);
            });
    },
    methods: {
        makeActive(ilac_id){
            let data = JSON.stringify({ "tcNum": this.tcNum, "ilac_id": ilac_id });
            const url5 = 'http://127.0.0.1:5000/makeActive';
            fetch(url5, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: data
            }).then(function (response) {
                console.log(response)
            }).then(function (text) {
                console.log(text);
            }).catch(function (error) {
                console.error(error);
            });
            this.resetPage()
        },
        resetPage() {
            setTimeout(function () { window.location.reload() }, 500);
        },
    },
}
</script>
