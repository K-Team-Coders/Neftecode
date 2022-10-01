<template>
    <body>
        <section class="bg-dark-gray">
            <Header></Header>
            <Carousel></Carousel>
            <!-- <div class="text-white border-white grid grid-rows-2 grid-cols-5">
                <div class="flex justify-center mr-36">
                    <div class="shadow-2xl mt-3">
                        <div class="flex justify-center mt-2">
                            <label for="small-input" class="flex text-lg font-medium text-gray-900 dark:text-gray-300">Битум: {{bitum}}%</label>
                        </div>
                        <div class="flex justify-center mt-3">
                            <input type="number" min="0" max="100" step="0.01" class=" p-2  text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="small-input"  v-model="bitum" placeholder="Введите % массы битума" />
                        </div>
                    </div>
                </div>
                <div class="mt-6 mr-4">
                    <div>
                        <label for="small-input" class="block text-center mb-2 text-lg font-medium text-gray-900 dark:text-gray-300">Связывающее вещество: {{ stapler }}%</label>
                    </div>
                    <div>
                        <input type="number" min="0" max="100" step="0.01" class="flex ml-20 p-2 w-1/2  text-gray-900 bg-gray-50 rounded-lg border border-gray-300 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="small-input" v-model="stapler" placeholder="Введите % массы сшивающей добавки" />
                    </div>                
                </div>
                <div>
                    <label for="countries" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400">Выберите тип полимера</label>
                        <select class="text-black" v-model="selected_polimer_type">
                            <option class="text-black" v-for="item in polimer.polimer_type" :key="item">{{item}}</option>
                        </select>
                        <div>
                            <p>Полимер:{{ polimer.polimer_mass }} %</p>
                            <input class="text-black" v-model="polimer.polimer_mass"
                                placeholder="Введите % массы полимера" />
                        </div>
                </div>

                <div>
                    <div>Выберите тип пластификатора
                    <select class="text-black" v-model="selected_plastificator_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-black" v-for="item in plastificator.plastificator_type" :key="item">{{item}}</option>
                    </select>
                    <span>Выбрано: {{selected_plastificator_type}}</span>
                    <div>
                        <p>пластификатор:{{plastificator.plastificator_mass }} %</p>
                        <input class="text-black" v-model="plastificator.plastificator_mass"
                            placeholder="Введите % массы пластификтора" />
                    </div>
                </div>
                </div>

                <div>
                    <div>Выберите тип адгезионной добавки
                    <select class="text-black" v-model="selected_adhesion_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-black" v-for="item in adhesion.adhesion_type" :key="item">{{item}}</option>
                    </select>
                    <span>Выбрано: {{selected_adhesion_type}}</span>
                    <div>
                        <p>Адгезионная добавка:{{ adhesion.adhesion_mass }} %</p>
                        <input class="text-black" v-model="adhesion.adhesion_mass"
                            placeholder="Введите % массы адгезионной добавка" />
                    </div>
                </div>
                </div>

                <div>
                    <div>Исходная игла при наклоне 25°
                        <p>:{{ needle_25 }} %</p>
                        <input class="text-black" v-model="needle_25" placeholder="Введите исходную иглу при 25°" />
                    </div>
                </div>

                <div>
                    <div>
                        <p>Базовой генерация для расчета пластификатора:{{ plastificator_generated }} %</p>
                        <input class="text-black" v-model="plastificator_generated" placeholder="Введите значение базовой генерации для расчета пластификатора" />
                    </div>
                </div>

                <div>
                    <div>
                        <p>Расчет рецептуры на глубину проникания иглы при 25°:{{ recept_needle_25 }} %</p>
                        <input class="text-black" v-model="recept_needle_25" placeholder="Введите значение расчета рецептуры на глубину проникания иглы при 25°" />
                    </div>
                </div>

            </div> -->

        <div class="px-32">
            <div class="grid grid-cols-6 grid-raws-3 gap-3 mt-4 text-black">
                <div class="col-start-1 col-end-3 py-2">
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Масса полимера: {{ polimer.polimer_mass }}%</label>
                    <select class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600" v-model="selected_polimer_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-white" v-for="item in polimer.polimer_type" :key="item">{{item}}</option>
                    </select>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input"  v-model="polimer.polimer_mass" placeholder="Введите % массы полимера" />
                </div>
                <div class="col-start-3 col-end-5 py-2"> 
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Масса пластификатора: {{plastificator.plastificator_mass }}%</label>
                    <select class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600" v-model="selected_plastificator_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-white" v-for="item in plastificator.plastificator_type" :key="item">{{item}}</option>
                    </select>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input" v-model="plastificator.plastificator_mass" placeholder="Введите % массы пластификтора" />
                </div> 
                <div class="col-start-5 col-end-7  py-2">
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Масса адгезионной добавки: {{ adhesion.adhesion_mass }}%</label>
                    <select class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600" v-model="selected_adhesion_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-white" v-for="item in adhesion.adhesion_type" :key="item">{{item}}</option>
                    </select>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input"  v-model="adhesion.adhesion_mass" placeholder="Введите % массы адгезионной добавки" />
                </div>          
                <div class="col-start-1 col-end-4 ">
                    <label class="flex justify-center font-bold text-2xl text-white mb-2">Битум: {{bitum}}%</label>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input"  v-model="bitum" placeholder="Введите % массы битума" />
                </div>
                <div class="col-start-4 col-end-7"> 
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Связывающее вещество: {{ stapler }}%</label>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input" v-model="stapler" placeholder="Введите % массы сшивающей добавки" />
                </div>
                <div class="col-start-1 col-end-3">
                    <label for="small-input" class="flex font-bold text-2xl text-white mb-2">Исходная игла<br> при наклоне 25°: {{ needle_25 }}</label>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input" v-model="needle_25" placeholder="Введите исходную иглу при 25°" />
                </div>
                <div class="col-start-3 col-end-5"> 
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Базовая генерация для расчета пластификатора: {{ plastificator_generated }} </label>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input" v-model="plastificator_generated" placeholder="Введите значение базовой генерации для расчета пластификатора"/>
                </div>
                <div class="col-start-5 col-end-7">
                    <label for="small-input" class="flex justify-center font-bold text-2xl text-white mb-2">Расчет рецептуры на глубину проникания иглы при 25°: {{ recept_needle_25 }}</label>
                    <input type="number" min="0" max="100" step="0.01" class="font-bold text-2xl text-center p-3 w-full mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 " id="small-input" v-model="recept_needle_25" placeholder="Введите значение расчета рецептуры на глубину проникания иглы при 25°" />
                </div>
            </div>
            <div class="flex justify-center mt-4 ">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-16 text-2xl rounded">
                    Рассчитать ФМС
                </button>
            </div>
        </div>         
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
            selected_plastificator_type:'',
            polimer: {
                polimer_type: [
                    'Polimer1', 'Polimer2', 'Polimer3', 'Polimer4'
                ],
                polimer_mass: 0
            },
            adhesion: {
                adhesion_type: [
                    'Не требуется', 'Adgesion1', 'Adgesion2','Adgesion3','Adgesion4'
                ],
                adhesion_mass: 0,
            },
            plastificator: {
                plastificator_type: [
                    'Plastificator1', 'Plastificator2', 'Plastificator1' ,'Plastificator1'
                ],
                plastificator_mass: 0
            }
        }
    },
    methods:{

}}

</script>

<style>
.underline-one {
    color: #f3f4f6;
    /* Цвет обычной ссылки */
    position: relative;
    cursor: pointer;
    text-decoration: none;
    /* Убираем подчеркивание */
}

.underline-one:after {
    content: "";
    display: block;
    position: absolute;
    right: 0;
    bottom: 3px;
    width: 0;
    height: 2px;
    /* Высота линии */
    background-color: rgb(255, 0, 0);
    /* Цвет подчеркивания при исчезании линии*/
    transition: width 0.5s;
    /* Время эффекта */
}

.underline-one:hover:after {
    content: "";
    width: 100%;
    display: block;
    position: absolute;
    left: 0;
    bottom: 3px;
    height: 2px;
    /* Высота линии */
    background-color: rgb(0, 38, 255);
    /* Цвет подчеркивания при появлении линии*/
    transition: width 0.5s;
    /* Время эффекта */
}
</style>
