<template>

    <body>
        <section class="bg-dark-gray">
            <Header></Header>
            <Carousel></Carousel>
            <div class="text-white border-white grid grid-rows-2 grid-cols-5">
                <div>
                    <div>
                        <p>Битум:{{ bitum }} %</p>
                        <input class="text-black" v-model="bitum" placeholder="Введите % массы битума" />
                    </div>
                </div>

                <div>
                    <div>
                        <p>Связывающее вещество:{{ stapler }} %</p>
                        <input class="text-black" v-model="stapler" placeholder="Введите % массы сшивающей добавки" />
                    </div>
                </div>

                <div>Выберите тип полимера
                    <select class="text-black" v-model="selected_polimer_type">
                        <option disabled value="">Выберите один из вариантов</option>
                        <option class="text-black" v-for="item in polimer.polimer_type" :key="item">{{item}}</option>
                    </select>
                    <span>Выбрано: {{selected_polimer_type}}</span>
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
