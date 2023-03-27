<template>
  <div id="home-section" class="d-flex align-items-end">
    <div class="container">
      <div class="row">
        <div class="col-12 text-center">
          <div class="logo mb-4 mt-3 mt-sm-0">
            <img class="img-fluid" src="../../../assets/main.png" alt="">

          </div>
          <div class="main-search position-relative mb-3">
            <span class="position-absolute left">
              <img src="../../../assets/search.png" alt="">
            </span>
            <multiselect title="Search" @select="selectPart($event)" @search-change="searchPart" v-model="selectedPart"
                         :options="partLists"
                         placeholder="Select a part"
                         label="title"
                         track-by="id"
            >

            </multiselect>
          </div>
          <div v-if="currentUrl === '/'"
               class="d-flex flex-column flex-sm-row justify-content-center">
            <a href="" class="rounded-3 search-item">Request Query</a>
            <a href="" class="rounded-3 search-item">Get Quotes</a>
            <a href="" class="rounded-3 search-item">Make Order</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import Multiselect from 'vue-multiselect'
import {mapGetters} from 'vuex'
import fs from "fs";


export default {
  components: {
    Multiselect
  },
  data() {
    return {
      currentUrl  : '',
      selectedPart: {},
      partLists   : [],
      searchImg   : "../../../assets/search.png",
    }
  },
  computed: {
    ...mapGetters(['parts']),
  },
  async mounted() {
    const conditions = ["part", "wizard"];
    if (!conditions.some(el => window.location.href.includes(el))) {
      this.$store.commit('emptyForm')
    }
    await this.getParts()
    await this.setSelectedPart()
    this.currentUrl = window.location.pathname;

    console.log(this.currentUrl);
  },
  methods: {
    async getParts(title = '') {
      await axios.get('/api/part/', {
        params: {
          'title': title
        }
      })
          .then(res => {
            this.partLists = res.data.results
          })
    },
    selectPart(event) {
      window.location.href = '/part/' + event.slug;
    },
    setSelectedPart() {
      let partSlug            = window.location.pathname.split("/").pop()
      const selectedPartInter = setInterval((e) => {
        this.selectedPart = {
          id   : this.parts.id,
          title: this.parts.title
        }
        if (partSlug == this.parts.slug) {
          clearInterval(selectedPartInter)
        }
      }, 100);

    },
    searchPart(query) {
      this.getParts(query)
    }
  },
}
</script>
