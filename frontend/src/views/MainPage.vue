<template>
  <body>
    <section class="bg-dark-gray">
      <Header></Header>
      <Carousel></Carousel>
      <div class="px-32">
        <div class="grid grid-cols-6 grid-raws-3 gap-3 mt-4 text-black">
          <div class="col-start-1 col-end-3 py-2">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-4"
              >Масса полимера: {{ polimer.polimer_mass }}%</label
            >
            <select
              class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600"
              v-model="selected_polimer_type"
            >
              <option disabled value="">Выберите один из вариантов</option>
              <option
                class="text-white"
                v-for="item in polimer.polimer_type"
                :key="item"
                >{{ item }}</option
              >
            </select>
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="polimer.polimer_mass"
              placeholder="Введите % массы полимера"
            />
          </div>
          <div class="col-start-3 col-end-5 py-2">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-4"
              >Масса пластификатора:
              {{ plastificator.plastificator_mass }}%</label
            >
            <select
              class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600"
              v-model="selected_plastificator_type"
            >
              <option disabled value="">Выберите один из вариантов</option>
              <option
                class="text-white"
                v-for="item in plastificator.plastificator_type"
                :key="item"
                >{{ item }}</option
              >
            </select>
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="plastificator.plastificator_mass"
              placeholder="Введите % массы пластификтора"
            />
          </div>
          <div class="col-start-5 col-end-7  py-2">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-4"
              >Масса адгезионной добавки: {{ adhesion.adhesion_mass }}%</label
            >
            <select
              class="font-bold p-2 w-1/2 mb-2 text-sm text-gray-100 rounded-lg border border-gray-300 bg-gray-700 dark:border-gray-600"
              v-model="selected_adhesion_type"
            >
              <option disabled value="">Выберите один из вариантов</option>
              <option
                class="text-white"
                v-for="item in adhesion.adhesion_type"
                :key="item"
                >{{ item }}</option
              >
            </select>
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="adhesion.adhesion_mass"
              placeholder="Введите % массы адгезионной добавки"
            />
          </div>
          <div class="col-start-1 col-end-4 ">
            <label
              class="flex justify-center font-bold text-2xl text-white mb-2"
              >Битум: {{ bitum }}%</label
            >
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="bitum"
              placeholder="Введите % массы битума"
            />
          </div>
          <div class="col-start-4 col-end-7">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-2"
              >Связывающее вещество: {{ stapler }}%</label
            >
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="stapler"
              placeholder="Введите % массы сшивающей добавки"
            />
          </div>
          <div class="col-start-1 col-end-3">
            <label
              for="small-input"
              class="flex font-bold text-2xl text-white mb-2"
              >Исходная игла<br />
              при наклоне 25°: {{ needle_25 }}</label
            >
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="needle_25"
              placeholder="Введите исходную иглу при 25°"
            />
          </div>
          <div class="col-start-3 col-end-5">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-2"
              >Базовая генерация для расчета пластификатора:
              {{ plastificator_generated }}
            </label>
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold p-3 w-full text-2xl text-center mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="plastificator_generated"
              placeholder="Введите значение базовой генерации для расчета пластификатора"
            />
          </div>
          <div class="col-start-5 col-end-7">
            <label
              for="small-input"
              class="flex justify-center font-bold text-2xl text-white mb-2"
              >Расчет рецептуры на глубину проникания иглы при 25°:
              {{ recept_needle_25 }}</label
            >
            <input
              type="number"
              min="0"
              max="100"
              step="0.01"
              class="font-bold text-2xl text-center p-3 w-full mb-2 text-gray-100 rounded-lg border border-gray-300  focus:ring-blue-500 focus:border-blue-500 bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 "
              id="small-input"
              v-model="recept_needle_25"
              placeholder="Введите значение расчета рецептуры на глубину проникания иглы при 25°"
            />
          </div>
        </div>
        <div class="flex justify-center mt-4 ">
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-16 text-2xl rounded"
          >
            Рассчитать ФМС
          </button>
        </div>

        <div class="overflow-x-auto relative mt-16 mb-3 rounded-lg">
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
      </div>
      <Footer></Footer>
    </section>
  </body>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import Carousel from '../components/Carousel.vue'
import axios from 'axios'
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

            mm_penetration_depth0: 0,
            mm_penetration_depth25: 0,
            cm_extensibility: 0,
            t_softening:0,
            t_elasticity: 0,

            polimer: {
                polimer_type: [
                    'Polymer1', 'Polymer2', 'Polymer3', 'Polymer4'
                ],
                polimer_mass: 0
            },
            adhesion: {
                adhesion_type: [
                    'Отсутствует', 'Adhesion1', 'Adhesion2','Adhesion3','Adhesion4'
                ],
                adhesion_mass: 0,
            },
            plastificator: {
                plastificator_type: [
                    'Plasticizer1', 'Plasticizer2', 'Plasticizer3' ,'Plasticizer4', 'Plasticizer5', 'Plasticizer6', 'Plasticizer7', 'Plasticizer8', 'Plasticizer9', 'Plasticizer10', 'Plasticizer11',
                    'Plasticizer12', 'Plasticizer13', 'Plasticizer14', 'Plasticizer15', 'Plasticizer16', 'Plasticizer17', 'Plasticizer18', 'Plasticizer19','Plasticizer20', 'Plasticizer21', 'Plasticizer22', 'Plasticizer23', 'Plasticizer24', 'Plasticizer25'
                ],
                plastificator_mass: 0
            },
        }


    },
    methods:{
        loadData() {
            let dataforloading = {'adhesion_mass': this.adhesion.adhesion_mass, 'bitum_mass': this.bitum, 'plasticizer_mass': this.plastificator.plastificator_mass, 
            'polymer_mass': this.polimer.polimer_mass, 'stapler_mass': this.stapler, 'needle_25': this.needle_25, 
            'adhesion_type': this.selected_adhesion_type, 'plasticizer_type': this.selected_plastificator_type, 'polimer_type': this.selected_polimer_type,
             'plasticizer_generated': this.plasticizer_generated, 'recept_needle_25': this.recept_needle_25}
            axios.post('http://127.0.0.1:8000/main/predict/',dataforloading)
            // .then (response => {
            //     this.mm_penetration_depth0
            //     this.mm_penetration_depth25
            //     this.cm_extensibility
            //     this.t_softening
            //     this.t_elasticity
            }
        }
}

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
  content: '';
  display: block;
  position: absolute;
  right: 0;
  bottom: 3px;
  width: 0;
  height: 2px;
  /* Высота линии */
  background-color: rgb(0, 251, 255);
  /* Цвет подчеркивания при исчезании линии*/
  transition: width 0.5s;
  /* Время эффекта */
}

.underline-one:hover:after {
  content: '';
  width: 100%;
  display: block;
  position: absolute;
  left: 0;
  bottom: 3px;
  height: 2px;
  /* Высота линии */
  background-color: rgb(0, 251, 255);
  /* Цвет подчеркивания при появлении линии*/
  transition: width 0.5s;
  /* Время эффекта */
}
</style>
