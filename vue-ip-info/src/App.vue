<template>
<header class="p-3 bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <h1>IP INFO</h1>
      </div>
    </div>
  </header>
    <section>
        <div class="container">
            <form @submit.prevent>
                <div class="row">
                <h4 class="hi-input">Enter your IP or select a text file:</h4>
                <div class="form-1 margin-form">
                    <div class="input-group">
                        <input v-bind:value="IP"  @input="IP = $event.target.value" type="text" class="form-control" placeholder="Enter your IP list in format x.x.x.x, x.x.x.x, ..., x.x.x.x" aria-label="Recipient's username with two button addons">
                        <button class="btn btn-outline-secondary" @click="getIpInfo" type="button">Enter</button>
                    </div>
                    <div class="mb-3" style="max-width: 240px;">
                            <input class="form-control form-control-sm" type="file" ref="file" accept="text/plain" id="formFile">
                    </div>
                </div>
                </div>
            </form>
        </div>
    </section>
    <section>
        <div class="container" v-if="ipInfoList.length==0&&failList.length==0" style="min-height: 300px;"></div>
        <div v-if="ipInfoList.length!=0||failList.length!=0" class="container" style="border: 1px solid teal; padding: 10px 15px;">
            <div class="row">
                <div class="col-5">
                   <div class="row" v-if="ipInfoList.length!=0">
                    <!-- <div class="d-flex justify-content-center"> -->
                        <ul v-for="item in ipInfoList" class="list-group">
                            <li class="list-group-item text-primary">IP : {{item.ip}}</li>
                            <li class="list-group-item">Internet Provider : {{item.int_prov}}</li>
                            <li class="list-group-item">Country : {{item.country}}</li>
                            <li class="list-group-item">City : {{item.city}}</li>
                            <li class="list-group-item">ZIP : {{item.zip}}</li>
                        </ul>
                    <!-- </div> -->
                    </div>
                    <br><br>
                   <div class="row" v-if="failList.length!=0">
                        <div class="fails">
                            <ul v-for="item in failList" class="list-group">
                                    <li class="list-group-item text-danger">Query : {{item.query}}</li>
                                    <li class="list-group-item text-danger">Status : {{item.status}}</li>
                                    <li class="list-group-item text-danger">Message : {{item.message}}</li>
                            </ul>
                        </div>
                   </div>
                </div>
                <div class="col-md-7" style="min-height: 400px">
                    <div id="map" class="map" style="width: 100%; height: 100%"></div>
                </div>
            </div>
        </div>
    </section>
    <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
        <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"></use></svg>
      </a>
      <span class="text-muted">Erastov Vyacheslav, 2022</span>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3"><a class="text-muted" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"></use></svg></a></li>
      <li class="ms-3"><a class="text-muted" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#instagram"></use></svg></a></li>
      <li class="ms-3"><a class="text-muted" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#facebook"></use></svg></a></li>
    </ul>
  </footer>
</template>

<script>

import axios from 'axios'

export default{

    data(){

        return{
            ipInfoList: [],
            failList: [],
            fail: '',
            ipInfo: '',
            IP: '',
            file: '',
            result: '',
            IPList: [],
        }

    },

    methods: {
        getIpInfo() {
            if(this.ipInfoList.length!=0){
                this.ipInfoList = [];
            }
            if(this.failList.length!=0){
                this.failList = [];
            }
            if(this.IP!=''){
                this.IPList = this.IP.split(', ');
                axios("http://localhost:8000/api/v1/ipinfo/ip/", {
                    method: 'POST',
                    async: true,
                    crossDomain: true,
                    data: this.IPList
                    }).then((response) => {
                        var list = [];
                            response.data.forEach(element => {
                                if(element.status=='success'){
                                    const ipInfo = {
                                        id: element.id,
                                        ip: element.ip,
                                        int_prov: element.int_prov,
                                        org: element.org,
                                        country: element.country,
                                        region_name: element.region_name,
                                        city: element.city,
                                        zip: element.zip,
                                        lat: element.lat,
                                        lon: element.lon,
                                    }
                                    this.ipInfo = ipInfo;
                                    this.ipInfoList.push(this.ipInfo);
                                    list.push(this.ipInfo);
                                }else{
                                    const fail = {
                                        query: element.query,
                                        status: element.status,
                                        message: element.message,
                                    }
                                    this.fail = fail;
                                    this.failList.push(this.fail);
                                    }
                                    })
                                    ymaps.ready(init);
                                    var map;
                                    function init(){
                                            map = new ymaps.Map('map', {
                                            center: [40, 40],
                                            zoom: 2,
                                            controls: ['zoomControl'],
                                            behaviors: ['drag']
                                        });
                                        list.forEach(element => {
                                        let center = [element.lat, element.lon];
                                        var placemark = new ymaps.Placemark(center, {
                                            hintContent: "IP: "+element.ip,
                                            balloonContent: [
                                                "IP: "+element.ip,
                                                '<br>',
                                                "Country: "+element.country,
                                                '<br>',
                                                "City: "+element.city,
                                            ].join('')
                                        });
                                        map.geoObjects.add(placemark);})
                                    }
                            })
                    .catch((error) => {
                    console.log(error)
                    })
                this.IP = '';
            } 
            else {
                this.file = this.$refs.file.files[0];
                let reader = new FileReader();
                reader.addEventListener("load", function () {
                    this.result=reader.result;
                    this.IPList = this.result.split(', ');
                    axios("http://localhost:8000/api/v1/ipinfo/ip/", {
                    method: 'POST',
                    async: true,
                    crossDomain: true,
                    data: this.IPList
                    }).then((response) => {
                        var list = [];
                            response.data.forEach(element => {
                                if(element.status=='success'){
                                    const ipInfo = {
                                        id: element.id,
                                        ip: element.ip,
                                        int_prov: element.int_prov,
                                        org: element.org,
                                        country: element.country,
                                        region_name: element.region_name,
                                        city: element.city,
                                        zip: element.zip,
                                        lat: element.lat,
                                        lon: element.lon,
                                    }
                                    this.ipInfo = ipInfo;
                                    this.ipInfoList.push(this.ipInfo);
                                    list.push(this.ipInfo);
                                }else{
                                    const fail = {
                                        query: element.query,
                                        status: element.status,
                                        message: element.message,
                                    }
                                    this.fail = fail;
                                    this.failList.push(this.fail);
                                    }
                                    })
                                ymaps.ready(init);
                                var map;
                                function init(){
                                        map = new ymaps.Map('map', {
                                        center: [40, 40],
                                        zoom: 2,
                                        controls: ['zoomControl'],
                                        behaviors: ['drag']
                                    });
                                    list.forEach(element => {
                                    let center = [element.lat, element.lon];
                                    var placemark = new ymaps.Placemark(center,{
                                        hintContent: "Ip: " + element.ip,
                                        balloonContent: [
                                                "IP: "+element.ip,
                                                '<br>',
                                                "Country: "+element.country,
                                                '<br>',
                                                "City: "+element.city,
                                            ].join('')
                                    }
                                    );
                                    map.geoObjects.add(placemark);})
                                }
                            })
                    .catch((error) => {
                    console.log(error)
                    })
                }.bind(this), false)
                reader.readAsText( this.file );
                }
            }
        }
    }
</script>

<style>
h1{
    color: teal;
}
.form-1{
    width: 66%;
    margin: 0 17%;
}
.hi-input{
    width: 30%;
    margin-top: 5%;
    color: teal;
    font-size: 100%;
    font-family: 'Arial';
    font-weight: 100;
    margin-left: 17.7%;
}
.margin-form{
    margin-bottom: 2%;
}
.input{
    width: 50%;
    margin: 0 25%;
    border: 1px solid teal;
    padding: 10px 15px;
}
.fails{
    display: flex;
    flex-wrap: wrap;
}
.btn{
    width: 90px;
    height: 40px;
    padding: 10px 15px;
    border: 1px solid teal;
    color: teal;
    font-size: 15px;
    font-family: 'Arial';
}

</style>