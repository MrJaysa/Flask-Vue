<script setup>
    import LoaderIcon from "./icons/lconLoader.vue";
</script>

<script>
    import { ref } from 'vue'
    // import { useIntersectionObserver } from '@vueuse/core'
    export default {
        data: () => ({
            currentPage: 1,
            data: null,
            has_next: false
        }),

        created() {
            this.fetchData()
        },

        watch: {
            // re-fetch whenever currentBranch changes
            currentPage: 'fetchData'
        },

        methods: {
            async fetchData() {
                let response = await (await fetch(`/api/get-data?page=${this.currentPage}`)).json();
                this.data = this.data ? this.data.concat(response.data) : response.data
                // if (this.data) {
                //     this.data.concat(response.data);
                // } else {
                //     this.data = response.data   
                // }
                this.has_next = response.has_next
            }
        },
    }
</script>

<template>
    <h2 class="mt-2">Fetched Data</h2>
    <div class="h-scroll">
        <div class="card" v-for="{ title, thumbnailUrl, url } in data">
            <img :src="`${thumbnailUrl}`" alt="photo">
            <p class="card-text">{{title}}</p>
        </div>
        <div id="loader">
            <LoaderIcon  />
        </div>
    </div>
</template>

<style scoped>
    .mt-2 {
        margin-top: 20px;
    }
    .h-scroll {
        overflow-x: scroll;
        white-space: nowrap;
        width: 600px;
        scroll-snap-type: x mandatory;
    }
    .h-scroll div {
        width: 200px;
        display: inline-block;
        scroll-snap-align: center;
    }

    img {
        width: 100%;
        height: 150px;
        border-radius: 10px;
    }
    
    .h-scroll div:nth-child(even) {
        margin: 20px
    }

    .card {
        background: white;
        border-radius: 11px;
        
    }
    
    .card-text {
        word-wrap: break-word;
        white-space: nowrap;
        text-overflow: ellipsis;
        color: black;
        width: 100%;
        overflow: hidden;
        padding: 5px
    }

    @media (max-width: 1023px) {
        .h-scroll {
            overflow-x: scroll;
            white-space: nowrap;
            width: 100%;
        }
    }

    .h-scroll::-webkit-scrollbar {
       width: 20px;
    }
    .h-scroll::-webkit-scrollbar-track {
        box-shadow: inset 0 0 5px grey; 
        border-radius: 10px;
    }

    .h-scroll::-webkit-scrollbar-thumb {
        background-color: rgb(134, 134, 134);
        border-radius: 10px;
    }
</style>

