<template>
    <div class="cinema_body">
        <Scroller>
            <ul>            
                <li v-for="item in cinemaList" :key="item.id">
                    <div>
                        <span>{{ item.nm }}</span>
                        <span class="q"><span class="price">{{ item.sellPrice}}</span> 元起</span>
                    </div>
                    <div class="address">
                        <span>{{ item.addr }}</span>
                        <span>{{ item.distance }}</span>
                    </div>
                    <div class="card">
                        <div v-for="(num, key) in item.tag" v-if="num===1" :key="key" :class=" key | classCard(key)">{{ key | formatCart(key) }}</div>
                    </div>
                </li>         
            </ul>
        </Scroller>
    </div>
</template>

<script>
export default {
    name : 'CiList',
    data(){
        return {
            cinemaList : [],
            prevCityId : -1
        };
    },
    activated(){
        var cityId = this.$store.state.city.id;
        if(cityId === this.prevCityId) {return;}

        this.axios.get('/api/cinemaList?cityId='+cityId).then((res) => {
            //console.log(res)
            var msg = res.data.msg;
            //console.log(msg);
            if(msg === 'ok'){
                this.cinemaList = res.data.data.cinemas;
                this.prevCityId = cityId; 
                //console.log(this.cinemaList);
            }
        })
    },
    filters : {
        formatCart(key){
            var card = [
                {key : 'allowRefund', value : '改签'},
                {key : 'buyout', value : '改签'},
                {key : 'cityCardTag', value : '改签'},
                {key : 'deal', value : '改签'},
                {key : 'endorse', value : '退票'},
                {key : 'sell', value : '折扣'},
                {key : 'snack', value : '小吃'},
                {key : 'vipTag', value : 'VIP'}
            ]

            for(var i=0; i<card.length; i++){
                //console.log(key)
                if(card[i].key === key){
                   return card[i].value; 
                }
            }
            return '';
        },
        classCard(key){
            var card = [
                {key : 'allowRefund', value : 'or'},
                {key : 'buyout', value : 'or'},
                {key : 'cityCardTag', value : 'or'},
                {key : 'deal', value : 'bl'},
                {key : 'endorse', value : 'bl'},
                {key : 'sell', value : 'or'},
                {key : 'snack', value : 'bl'},
                {key : 'vipTag', value : 'or'}
            ]

            for(var i=0; i<card.length; i++){
                //console.log(key)
                if(card[i].key === key){
                   return card[i].value; 
                }
            }
            return '';
        }       
    }
}
</script>

<style scoped>
#content .cinema_body{ flex:1; overflow:auto;}
.cinema_body ul{ padding:20px;}
.cinema_body li{  border-bottom:1px solid #e6e6e6; margin-bottom: 20px;}
.cinema_body div{ margin-bottom: 10px;}
.cinema_body .q{ font-size: 11px; color:#f03d37;}
.cinema_body .price{ font-size: 18px;}
.cinema_body .address{ font-size: 13px; color:#666;}
.cinema_body .address span:nth-of-type(2){ float:right; }
.cinema_body .card{ display: flex;}
.cinema_body .card div{ padding: 0 3px; height: 15px; line-height: 15px; border-radius: 2px; color: #f90; border: 1px solid #f90; font-size: 13px; margin-right: 5px;}
.cinema_body .card div.or{ color: #f90; border: 1px solid #f90;}
.cinema_body .card div.bl{ color: #589daf; border: 1px solid #589daf;}    
</style>
