const searchBtn = document.getElementById("search-button");
const searchInput = document.getElementById("search-input");

const spriteDiv = document.getElementById("sprite");
const nameP = document.getElementById("pokemon-name");
const id = document.getElementById("pokemon-id");
const weight = document.getElementById("weight");
const height = document.getElementById("height");
const types = document.getElementById("types");
const hp = document.getElementById("hp");
const attack = document.getElementById("attack");
const defense = document.getElementById("defense");
const specialAttack = document.getElementById("special-attack");
const specialDefense = document.getElementById("special-defense");
const speed = document.getElementById("speed");

const fetchPokemon = async (search) => {
    try{
        const answer = await fetch(`https://pokeapi-proxy.freecodecamp.rocks/api/pokemon/${search}`);
        const pokemon = await answer.json();
        console.log(pokemon);
        return pokemon;

    }catch(err){
        throw new Error('Pokemon not found');
    }
}

const setPokemonValues = (pokemon) => {
    types.innerHTML = pokemon.types.map((obj) => `<span class="type ${obj.type.name}">${obj.type.name}</span>`).join('');

    spriteDiv.innerHTML = `<img id="sprite" src="${pokemon.sprites.front_default}" alt="${pokemon.name} front default sprite">`;
    
    nameP.textContent           = pokemon.name.toUpperCase()
    id.textContent             = pokemon.id
    weight.textContent         = pokemon.weight
    console.log(pokemon)
    height.textContent         = pokemon.height
    hp.textContent             = pokemon.stats[0].base_stat
    attack.textContent         = pokemon.stats[1].base_stat
    defense.textContent        = pokemon.stats[2].base_stat
    specialAttack.textContent  = pokemon.stats[3].base_stat
    specialDefense.textContent = pokemon.stats[4].base_stat
    speed.textContent          = pokemon.stats[5].base_stat
}

const searchPokemon = async () => {
    const search = searchInput.value.toLowerCase();
    if(!search) return

    try{
        const pokemon = await fetchPokemon(search);
        setPokemonValues(pokemon);
    }catch (err){
        alert(err.message)
    }
    
}

searchBtn.addEventListener("click", searchPokemon);