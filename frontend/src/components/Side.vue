<script setup>
  import Item from "./Item.vue";
  import Image from "./Image.vue";
  import DocumentationIcon from "./icons/IconDocumentation.vue";
  import ToolingIcon from "./icons/IconTooling.vue";
</script>

<template>
  <div>
    <Item>
      <template #icon>
        <DocumentationIcon />
      </template>
  
      <template #heading>Introduction</template>
      <div>
        <p>
          This project showcases the integration of vuejs into python flask web micro-framework. The python flask serves as the backend server and vuejs is used for developing the frontend.
        </p>
      </div>
    </Item>
    
    <Item>
      <template #icon>
        <ToolingIcon />
      </template>
      <template #heading>Api</template>
      <div>
        <p>
          The data shown below are derived from <a target="_blank" href="https://jsonplaceholder.typicode.com/">Jsonplaceholder</a>, which provides prototyping data and you can visit their site to find out more.
        </p>
        <p>
          The data provided for images cannot be queried in batches thus, the python flask web micro-framework came to our rescue. Helping us to deliver data when need at the moment it is instead of loading the entire 5000 record and overpopulating our webpage as well as serving our vue application.
        </p>
        <p>
          The api use in this application can be accessed <a target="_blank" href="/api/get-data?page=1">here</a> or copy and paste the link 'http://app.com/api/get-data'; The link provides data in json format with ten records per page 
        </p>
      </div>
    </Item>
  
    <Image/>
  </div>
  
</template>


<style scoped>
p {
  margin-top: 10px !important;
}
</style>