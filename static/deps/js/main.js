getSortedFilm = () => {
    const howSort = document.querySelector(".howSort")
    howSort.innerHTML = `<p class="movieSelection">
    <div class="sortdiv">
        <img
        alt=""
        class="installjacija"
        src="https://static.overlay-tech.com/assets/3a9b159f-cd3f-4d99-a433-b2a36feb5b42.svg"
        />
        <div style="margin: 50px 50px 0px 0px">
            <input onclick="whiSort(1)" type="radio" name="Filter" value="" checked="checked">Инсталляция
        </div>
    </div>
    <div class="sortdiv">
        <img
        alt=""
        class="skul-ptura"
        src="https://static.overlay-tech.com/assets/9d1cddc1-9877-475d-a4e2-162a7d1d6982.svg"
        />
        <div style="margin: 50px 50px 0px 0px">
            <input onclick="whiSort(2)" type="radio" name="Filter" value="">Скульптуры, статуи
        </div>
    </div>
    <div class="sortdiv">
        <img
        alt=""
        class="stenografija"
        src="https://static.overlay-tech.com/assets/dc82ad64-076e-4961-aeb7-2479041cf6de.svg"
        />
        <div style="margin: 50px 50px 0px 0px">
            <input onclick="whiSort(3)" type="radio" name="Filter" value="">Стенография 
        </div>
    </div>
    <div class="sortdiv">
        <img
        alt=""
        class="skul-ptura"
        src="https://static.overlay-tech.com/assets/1d7c15fa-bcf1-4405-844e-e93466963830.svg"
        />
        <div style="margin: 50px 50px 0px 0px">
            <input onclick="whiSort(4)" type="radio" name="Filter" value="">Стела
        </div>
    </div>
    <button onclick="sortFilms()" class="bottomSort"><span class="material-symbols-outlined">check</span></button>
    </p>`
}


