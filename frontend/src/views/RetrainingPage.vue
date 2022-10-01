<template>

    <body>
        <section class="bg-dark-gray">
            <Header></Header>
            <section class="bg-dark-gray">
                <div class="flex justify-center">
                    <form class="flex bg-white items-center mr-12 mt-12">
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
export default {
    components: { Header, Footer, Carousel },
    data() {
        return {
            bitum: 0,
            stapler: 0,
            needle_25: 0,
            plastificator_generated: 0,
            recept_needle_25: 0,
            selected_polimer_type: '',
            selected_adhesion_type: '',
            selected_plastificator_type: '',
            polimer: {
                polimer_type: [
                    'Polimer1', 'Polimer2', 'Polimer3', 'Polimer4'
                ],
                polimer_mass: 0
            },
            adhesion: {
                adhesion_type: [
                    'Не требуется', 'Adgesion1', 'Adgesion2', 'Adgesion3', 'Adgesion4'
                ],
                adhesion_mass: 0,
            },
            plastificator: {
                plastificator_type: [
                    'Plastificator1', 'Plastificator2', 'Plastificator1', 'Plastificator1'
                ],
                plastificator_mass: 0
            }
        }
    },
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
            )},

        handleFileUpload() {
            this.file = this.$refs.file.files[0]
        }
    }
}
</script>

<style>

</style>
