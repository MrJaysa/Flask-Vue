<!-- <template>
  <h2>Fetched Data</h2>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae dignissimos, doloremque et magnam dicta beatae porro eligendi. Optio id beatae magni quisquam aspernatur fuga consequuntur deleniti cum. Odit, sequi perferendis?
  </p> 
</template>


<style scoped>
p {
  margin-top: 10px !important;
}
</style> -->


<script>
    const API_URL = `https://api.github.com/repos/vuejs/core/commits?per_page=3&sha=`

    export default {
    data: () => ({
        branches: ['main', 'v2-compat'],
        currentBranch: 'main',
        commits: null
    }),

  created() {
    this.fetchData()
  },

  watch: {
    // re-fetch whenever currentBranch changes
    currentBranch: 'fetchData'
  },

  methods: {
    async fetchData() {
      const url = `${API_URL}${this.currentBranch}`
      this.commits = await (await fetch(url)).json()
    },
    truncate(v) {
      const newline = v.indexOf('\n')
      return newline > 0 ? v.slice(0, newline) : v
    },
    formatDate(v) {
      return v.replace(/T|Z/g, ' ')
    }
  }
}
</script>

<template>
  <h1>Latest Vue Core Commits</h1>
  <template v-for="branch in branches">
    <input type="radio"
      :id="branch"
      :value="branch"
      name="branch"
      v-model="currentBranch">
    <label :for="branch">{{ branch }}</label>
  </template>
  <p>vuejs/vue@{{ currentBranch }}</p>
  <ul>
    <li v-for="{ html_url, sha, author, commit } in commits">
      <a :href="html_url" target="_blank" class="commit">{{ sha.slice(0, 7) }}</a>
      - <span class="message">{{ truncate(commit.message) }}</span><br>
      by <span class="author">
        <a :href="author.html_url" target="_blank">{{ commit.author.name }}</a>
      </span>
      at <span class="date">{{ formatDate(commit.author.date) }}</span>
    </li>
  </ul>
</template>