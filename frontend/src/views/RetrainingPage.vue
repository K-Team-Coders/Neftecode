<template>

    <body>
        <section class="bg-dark-gray h-screen">
            <Header></Header>
            <section class="bg-dark-gray">
                <div class="flex justify-center mt-12">
                    <h1 class="text-6xl text-white opacity-85">
                        Переобучение модели
                    </h1>
                </div>
                <div class="flex justify-center mt-20">
                    <form class="flex bg-white items-center mr-12">
                        <label class="block">
                            <input accept=".csv" type="file" class="block w-full text-xl mr-52 font-rale text-slate-500
                     file:mr-0 file:py-4 file:px-10
                     file:border-0
                     file:text-xl file:font-semibold
                     file:bg-violet-100 file:text-violet-700
                     hover:file:bg-pink-200
                     " ref="file" v-on:change="handleFileUpload()" />
                        </label>
                        <button
                            class="ml-32 font-rale bg-violet-50 hover:bg-green-200 text-violet-700 text-xl font-semibold  py-3 px-7"
                            @click="submitFile()">
                            Загрузить
                        </button>
                    </form>
                    <div>
                        <Heatmap></Heatmap>
                    </div>
                    
                        
                </div>
                <!-- <div class="flex justify-center px-1 py-2 mt-10 ml-16 border">
                    <h5 class="flex font-italic text-white text-center font-rale tracking-widest justify-center mt-3">{x: Названия таблиц; y: Количество обращений}</h5>
                    <div class="flex">
                      <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-white mr-2">{{this.sum_into}}</div>
                          </div>
                          <div class="text-lg text-white font-corme">Общее количество JOIN</div>
                        </div>
                      </div>
                      <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-white mr-2">{{this.sum_froms}}</div>
                          </div>
                          <div class="text-lg text-white font-corme">Общее количество FROM</div>
                        </div>
                      </div>
                      <div class="flex items-center py-2">
                        <div class="mr-5">
                          <div class="flex items-center justify-center">
                            <div class="text-3xl font-bold text-white mr-2">{{this.sum_into}}</div>
                            <div class="text-sm font-medium text-yellow-500"></div>
                          </div>
                          <div class="text-lg text-white font-corme">Общее количество INTO</div>
                        </div>
                      </div>
                    </div>
                </div>
                <div class="flex justify-start mb-3 mt-12 ml-12 border-2">
                    <Scatter :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId"
                      :dataset-id-key="datasetIdKey" :plugins="plugins" :css-classes="cssClasses" :styles="styles"
                      :width="width" :height="height" />
                      ssssssssssssssssssss
                </div> -->

                <div class="overflow-x-auto relative mt-16 px-10 mb-3 rounded-lg">
                    <table
                        class="w-full text-sm text-center bg-gray-700 text-white"
                    >
                        <thead
                        class=" text-white text-base uppercase bg-gray-700 "
                        >
                        <tr>
                            <th scope="col" class="py-3 border">
                            Глубина проникания иглы при 0 °С, [мм-1]
                            </th>
                            <th scope="col" class="py-3 border">
                            Глубина проникания иглы при 25 °С, [мм-1]
                            </th>
                            <th scope="col" class="py-3 border">
                            Растяжимость при температуре 0 °С, [см]  
                            </th>
                            <th scope="col" class="py-3 border">
                            Температура размягчения, [°С]
                            </th>
                            <th scope="col" class="py-3 border">
                            Эластичность при 0 °С, [%]
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr
                            class="border-b bg-gray-800 border-gray-700"
                        >
                            <td class="py-6 px-6 border text-center text-5xl">
                            {{mm_penetration_depth0}}
                            </td>
                            <td class="py-6 px-6 border text-center text-5xl">
                            {{mm_penetration_depth25}}
                            </td>
                            <td class="py-6 px-6 border text-center text-5xl">
                            {{cm_extensibility}}
                            </td>
                            <td class="py-6 px-6 border text-center text-5xl">
                            {{t_softening}}
                            </td>
                            <td class="py-6 px-6 border text-center text-5xl">
                            {{t_elasticity}}
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </section>
            <Footer></Footer>
        </section>
    </body>
</template>

<script>

import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import Carousel from '../components/Carousel.vue'
import Heatmap from "../components/charts/Heatmap.vue";


export default {
    components: { Heatmap, Header, Footer, Carousel },
            methods: {
            submitFile() {
                let formData = new FormData();
                formData.append('file', this.file);
                axios.post('http://127.0.0.1:8000/main/load_file_tables/',
                    formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                )
            },

            handleFileUpload() {
                this.file = this.$refs.file.files[0]
            }
        }
}

</script>

<style>

</style>
