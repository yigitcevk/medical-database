<template>
    <div style=' heigth : 100vh'>
        <div style="myCars">
            <h3>
                Profile:
            </h3>
            <p>
                Eczane Ismi : {{ eczaneAd }}
            </p>
            <p>
                Adres : {{ eczaneAdres }}
            </p>
            <p>
                Eczaci Isim ve Soyisim : {{ eczaciAdSoyad }}
            </p>
            <p>
                Eczaci Id : {{ eczaciId }}
            </p>
        </div>

        <div>
            <table border="1" style="background-color: #656569;">
                <thead>
                    <tr>
                        <th>İlaç Adı</th>
                        <th>Alış Fiyatı</th>
                        <th>Satış Fiyatı</th>
                        <th>İlaç Sayısı</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in ilaclar" :key="item.ilac_id">
                        <td>{{ item.ilac_ad }}</td>
                        <td>{{ item.alis_fiyat }}</td>
                        <td>{{ item.satis_fiyat }}</td>
                        <td>{{ item.envanter }}</td>
                        <td><button class='button-black' @click="removeMedicine(item.ilac_id)">
                                İlaç sayısını eksilt
                            </button></td>
                    </tr>
                </tbody>
                <thead>
                    <tr>
                        <th>Per tcno</th>
                        <th>Personel isim</th>
                        <th>Personel tel no</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in personeller" :key="item.ilac_id">
                        <td>{{ item.per_tckn }}</td>
                        <td>{{ item.per_ad_soyad }}</td>
                        <td>{{ item.per_tel_no }}</td>
                        <td><button class='button-black' @click="removePer(item.per_tckn)">
                                İşten çıkar
                            </button></td>
                    </tr>
                </tbody>
                <button class='button-black' @click="$router.go(-1)">Geri Dön</button>
            </table>

            <div class="container" style="text-align: left; align-items: left">
                <div class='addMedicineCard' style="border-style: solid;">
                    <div>
                        <div>
                            <label for="enter-email" style="margin-top: 5px; margin-right: 5px;">İlaç ID</label>
                            <input style="border-style: solid; margin-top: 5px;" v-model="ilac_id"
                                v-on:keyup.enter="login" placeholder="İlaç Id giriş" />

                            <label for="enter-email" style="margin-top: 5px; margin-right: 5px;">İlaç Adı</label>
                            <input style="border-style: solid; margin-top: 5px;" v-model="ilac_ad"
                                v-on:keyup.enter="login" placeholder="İlaç adı giriş" />
                        </div>

                        <div>
                            <label for="enter-email" style="margin-top: 5px; margin-right: 5px;">Alış Fiyatı</label>
                            <input style="border-style: solid; margin-top: 5px;" v-model="alis_fiyat"
                                v-on:keyup.enter="login" placeholder="Alış fiyatı giriş" />
                            <label for="enter-email" style="margin-top: 5px; margin-right: 5px;">Satış Fiyatı</label>
                            <input style="border-style: solid; margin-top: 5px;" v-model="satis_fiyat"
                                v-on:keyup.enter="login" placeholder="Satış fiyatı giriş" />
                        </div>
                        <div>
                            <label for="enter-email" style="margin-top: 5px; margin-right: 5px;">Envanter</label>
                            <input style="border-style: solid; margin-top: 5px;" v-model="envanter"
                                v-on:keyup.enter="login" placeholder="Miktar giriş" />
                        </div>
                    </div>

                    <a class="button-login" @click="addMedicine()">
                        Ekle
                    </a>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'EczaneAdmin',
    components: {
    },
    data() {
        return {
            eczaneId: null,
            eczaneAd: "",
            eczaneAdresId: null,
            eczaneAdres: "",
            eczaciAdSoyad: "",
            eczaciId: null,
            ilaclar: [],
            ilac_id: null,
            ilac_ad: "",
            alis_fiyat: "",
            satis_fiyat: "",
            envanter: "",
            personelAdSoyad: "",
            pertckn: "",
            personeller: []

        }
    },
    created() {
        const pageInfo = this.$router.currentRoute.value;
        console.log(this.$router.currentRoute.value);
        this.eczaneId = pageInfo.params.eczaneID

        const url1 = 'http://127.0.0.1:5000' + pageInfo.fullPath;
        fetch(url1)
            .then(async response => {
                const data = await response.json();
                if (!response.ok) {
                    const error = (data && data.message) || response.statusText;
                    return Promise.reject(error);
                }
                this.eczaneAd = data[1].eczane_ad
                this.eczaneAdresId = data[1].adres_id

                const url2 = 'http://127.0.0.1:5000/adres/' + this.eczaneAdresId;
                fetch(url2)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        this.eczaneAdres = data[1].il + " " + data[1].ilce + " " + data[1].posta_kodu;
                    })
                    .catch(error => {
                        this.errorMessage = error;
                        console.error("There was an error!", error);
                    });

                const url3 = 'http://127.0.0.1:5000/eczaci/' + this.eczaneId;
                fetch(url3)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        this.eczaciAdSoyad = data[1].eczaci_ad_soyad
                        this.eczaciId = data[1].eczaci_id
                    })
                    .catch(error => {
                        this.errorMessage = error;
                        console.error("There was an error!", error);
                    });
                const url9 = 'http://127.0.0.1:5000/personel/' + this.eczaneId;
                fetch(url9)
                    .then(async response => {
                        const data = await response.json();
                        if (!response.ok) {
                            const error = (data && data.message) || response.statusText;
                            return Promise.reject(error);
                        }
                        data.forEach(element => {
                            console.log(element)
                            if (element['eczane_id'] != 0) {
                                this.personeller.push(element)
                            }
                        });
                        //this.personeller=data;
                        //this.personelAdSoyad = data[1].personel_ad_soyad
                        //this.pertckn = data[1].per_tckn
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

    },
    methods: {
        removeMedicine(ilac_id) {
            let data = JSON.stringify({ "ilac_id": ilac_id, "eczane_id": this.eczaneId });
            const url5 = 'http://127.0.0.1:5000/removeMedicine';
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
            this.resetPage();
        },
        resetPage() {
            setTimeout(function () { window.location.reload() }, 500);
        },
        removePer(pertckn) {
            let data = JSON.stringify({ "per_tckn": pertckn, "eczane_id": this.eczaneId });
            const url10 = 'http://127.0.0.1:5000/removePer';
            fetch(url10, {
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
            this.resetPage();
        },
        addMedicine() {
            let data = JSON.stringify({ "alis_fiyat": this.alis_fiyat, "eczane_id": this.eczaneId, "envanter": this.envanter, "ilac_ad": this.ilac_ad, "ilac_id": this.ilac_id, "satis_fiyat": this.satis_fiyat });

            const url20 = 'http://127.0.0.1:5000/addMedicine';
            console.log(url20)
            fetch(url20, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                    'mode': 'no-cors'
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
        }
    },
}
</script>

<style>
.input {
    width: 250px;
    border-radius: 8px;
}

.addMedicineCard {
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
    /* This bit draws the box around it */
    background: #ffffff;
    /* Shadow / 1 */
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.05), 0px 25px 35px rgba(0, 0, 0, 0.03);
    border-radius: 8px;
    width: 40%;
}

.container {
    display: flex;
    align-items: left;
    justify-content: center;
    flex-direction: column;
    width: 100%;
    text-align: left;
    align-items: left;
    margin-top: 10px;
}
</style>