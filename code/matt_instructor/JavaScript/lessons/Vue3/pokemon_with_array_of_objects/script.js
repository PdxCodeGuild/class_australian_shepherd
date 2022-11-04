const app = Vue.createApp({
    data(){
        return{
            pokemon: [
                {
                    name: 'pikachu',
                    id: 25,
                    type: 'electric'
                },
                {
                    name: 'goldeen',
                    id: 118,
                    type: 'water'
                },
                {
                    name: 'snorlax',
                    id: 143,
                    type: 'normal'
                },
                {
                    name: 'charizard',
                    id: 6,
                    type: 'fire'
                },
                {
                    name: 'mewtwo',
                    id: 150,
                    type: 'psychic'
                },
                {
                    name: 'gengar',
                    id: 94,
                    type: 'ghost'
                },
                {
                    name: 'jigglypuff',
                    id: 39,
                    type: 'normal'
                },
                {
                    name: 'squirtle',
                    id: 7,
                    type: 'water'
                }
            ],
            pokemonImage: ''
        }
    },
    methods:{
        getPokeInfo(poke){
            axios({
                method: 'get',
                url: `https://pokeapi.co/api/v2/pokemon/${poke.name}`,
            }).then((response) => {
                this.pokemonImage = response.data.sprites.front_default
            })
        }
    },
    setup(){
        
    }
})