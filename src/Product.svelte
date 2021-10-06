<script>
    export let json_data;
    //json_data format
    // "data-brand": "Ferz",
    // let json_data = {
    //     "data-category": "\u0420\u0401\u0420\u00b0\u0420\u0457\u0420\u0454\u0420\u0451",
    //     "data-color-family": "\u0421\u2021\u0420\u00b5\u0421\u0402\u0420\u0405\u0421\u2039\u0420\u2116",
    //     "data-discount": "189",
    //     "data-discount-percent": "15",
    //     "data-gallery": [
    //         "./img236x341/F/E/FE913CMCLMM1_7110810_1_v1.jpg",
    //         "./img236x341/F/E/FE913CMCLMM1_7110811_2_v1.jpg",
    //         "./img236x341/F/E/FE913CMCLMM1_7110812_3_v1.jpg",
    //         "./img236x341/F/E/FE913CMCLMM1_7110813_4_v1.jpg",
    //         "./img236x341/F/E/FE913CMCLMM1_7113609_9_v1.jpg",
    //     ],
    //     "data-gender": "men",
    //     "data-href": "https://www.lamoda.ru/p/fe913cmclmm1/hats-ferz-shapka/",
    //     "data-is-new": "false",
    //     "data-is-premium": "false",
    //     "data-is-sport": "false",
    //     "data-name": "\u0420\u0401\u0420\u00b0\u0420\u0457\u0420\u0454\u0420\u00b0",
    //     "data-price": "1010",
    //     "data-price-origin": "1199",
    //     "data-season":
    //         "{5593:\u0420\u00b7\u0420\u0451\u0420\u0458\u0420\u00b0,5595:\u0420\u0491\u0420\u00b5\u0420\u0458\u0420\u0451\u0421\u0403\u0420\u00b5\u0420\u00b7\u0420\u0455\u0420\u0405}",
    //     "data-sku": "FE913CMCLMM1",
    //     "data-src": "./img236x341/F/E/FE913CMCLMM1_7110810_1_v1.jpg",
    // };
    let image_src = json_data["data-src"];
    let image_urls = json_data["data-gallery"];
    let is_item__extra_visible = false;
    function set_list_item__extra_visible_on_MouseEnter() {
        is_item__extra_visible = true;
    }
    function set_list_item__extra_invisible_on_MouseOut(e) {
        is_item__extra_visible = false;
        set_image_default();
    }
    function set_image_default() {
        image_src = json_data["data-src"];
    }

    function change_image_src(e) {
        image_src = image_urls[e.target.dataset.id];
    }
</script>

<div
    class="products-list-item"
    data-type="category"
    data-rollover="./img236x341/M/P/MP002XM1RK04_15191679_2_v1_2x.jpg"
    on:mouseenter={set_list_item__extra_visible_on_MouseEnter}
    on:mouseleave={set_list_item__extra_invisible_on_MouseOut}
>
    <a href={json_data["data-href"]} data-position="2" class="products-list-item__link link">
        <div class="product-list-item__gallery">
            {#each image_urls as val, i}
                <div class="product-list-item__gallery-page" data-id={i} on:mouseenter={change_image_src} />
            {/each}
        </div>
        <div
            class="to-favorites js-to-favorites                      to-favorites_wish-groups"
            data-sku="MP002XM1RK04"
            data-image="./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg"
            data-price-origin={json_data["data-price-origin"]}
            data-gender="men"
            data-name="Пуловер"
            data-color-family="коричневый"
            data-brand="Zolla"
            data-is-sport="false"
            data-is-premium="false"
            data-season="5592:мульти"
            data-is-new="false"
            data-category="Джемперы, свитеры и кардиганы"
        />
        <div class="products-list-item_labels">
            <div class="products-list-item_placeholder" />
            <div
                class="js-wish-arrow-open arrow-svg-bottom arrow-svg-bottom_grey
                wish-groups__arrow wish-groups__arrow_closed"
                data-sku="MP002XM1RK04"
            />

            <img
                src={image_src}
                class="products-list-item__img"
                width="236"
                height="341"
                alt="{json_data['data-name']}, {json_data['data-brand']}, цвет: {json_data[
                    'data-color-family'
                ]}. Артикул: {json_data['data-sku']}. Одежда / {json_data['data-category']}"
            />

            <span class="vue-widget product-list-item__badges">
                <!---->
            </span>
        </div>
        <span class="price">
            {#if json_data.hasOwnProperty("data-price")}
                <span class="price__actual parts__price_cd-disabled">
                    {json_data["data-price-origin"].toLocaleString()}
                </span>
                <span class="price__action js-cd-discount ">
                    {json_data["data-price"].toLocaleString()}
                </span>
            {:else}
                <span class="price__actual">{json_data["data-price-origin"].toLocaleString()}</span>
            {/if}
            <span class="price__currency">&nbsp;₽</span>
        </span>
        <div class="products-list-item__brand">
            {json_data["data-brand"]}
            <span class="products-list-item__type"> {json_data["data-name"]} </span>
        </div>
    </a>
    <div class="groups-by-sku groups-by-sku_hidden" />
    <div class="products-list-item_blur" />
    {#if is_item__extra_visible == true}
        <div class="products-list-item__extra">
            <div class="products-list-item__extra-info">
                {#if Array.isArray(json_data["data-sizes"]) && json_data["data-sizes"].length}
                    <div class="products-list-item__sizes">
                        <span class="products-list-item__sizes-title"> Размеры (RUS): </span>
                        {#each json_data["data-sizes"] as size}
                            <a
                                class="products-list-item__size-item link"
                                href="{json_data['data-href']}?sku={json_data['data-sku']}"
                            >
                                {size}
                            </a>
                        {/each}
                    </div>
                {/if}
                <div
                    class="zoomin products-list-item__qv"
                    data-sku="MP002XM1RK04"
                    data-position="2"
                    data-quick="MP002XM1RK04"
                    data-quick-type="category"
                    data-quick-promotion-provider-id=""
                >
                    Подробнее
                </div>
            </div>
        </div>
    {/if}
</div>

<style>
    .products-list-item__extra {
        /* display: none; */
        position: absolute;
        top: -11px;
        right: -11px;
        left: -11px;
        background: #fff;
        color: #888;
    }

    .not-touch .products-list-item:hover .products-list-item__extra {
        display: block;
    }

    .product-list-item__gallery {
        display: none;
        position: absolute;
        top: 2px;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 2;
    }

    .products-list-item__link:hover .product-list-item__gallery {
        display: flex;
    }

    .product-list-item__gallery-page {
        position: relative;
        display: flex;
        align-items: flex-end;
        flex: 1;
        height: 100%;
    }

    .product-list-item__gallery-page:after {
        content: "";
        position: absolute;
        top: 0;
        left: 2px;
        right: 2px;
        height: 3px;
        border-radius: 2px;
        opacity: 0.3;
        background: #888;
    }

    .product-list-item__gallery-page:hover {
        height: 100%;
    }

    .product-list-item__gallery-page:hover::after {
        opacity: 1;
        background: #888;
    }

    .products-list-item__qv {
        position: relative;
        top: auto;
        width: 256px;
        background-color: #fff;
    }

    .products-list-item__extra-info {
        position: absolute;
        line-height: 17px;
        top: 100%;
        background: #fff;
    }

    .products-list-item__extra-info:after {
        display: block;
        width: 100%;
        top: -10px;
        left: 0;
        background: #fff;
    }

    .products-list-item__extra-info .products-list-item__sizes {
        padding: 0 10px 10px;
    }

    .products-list-item__qv:after {
        content: "";
    }

    .products-list-item__link {
        display: block;
        z-index: 2;
        position: relative;
    }

    .products-list-item__img {
        position: absolute;
        top: 0;
        left: 0;
        display: block;
        width: 236px;
        height: 340px;
    }

    .products-list-item {
        display: inline-block;
        vertical-align: top;
        width: 236px;
        margin: 0 10px 35px 0;
        position: relative;
    }

    .products-list-item:hover {
        z-index: 3;
    }

    .products-list-item__brand {
        color: #000;
        margin-top: 7px;
    }

    .products-list-item .price {
        display: block;
        font-size: 16px;
        padding-top: 351px;
    }

    .products-list-item__type,
    .products-list-item__type::after {
        color: #888;
        position: relative;
        z-index: 1;
        padding-bottom: 2px;
    }

    .products-list-item__type::before {
        content: " / ";
    }

    .products-list-item__sizes {
        position: relative;
        z-index: 1;
    }

    .products-list-item__sizes-title {
        margin-right: 5px;
        color: #888;
    }

    .products-list-item__size-item {
        display: inline-block;
        margin-right: 5px;
    }

    .products-list-item_labels {
        height: 0;
        font-size: 0;
    }

    .products-list-item_placeholder {
        display: inline-block;
        position: absolute;
        background-color: #f5f5f5;
        width: 236px;
        height: 341px;
    }

    .products-list-item__extra {
        bottom: -11px;
    }

    .products-list-item__extra-info:after {
        content: "";
        height: 0;
        position: absolute;
    }

    .products-list-item__extra {
        border: 0;
        box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
    }

    .products-list-item__extra-info {
        border: 0;
        box-shadow: 0 3px 4px rgba(0, 0, 0, 0.1);
        left: 0;
        right: 0;
        z-index: 3;
        margin-top: 0;
    }

    .not-touch .products-list-item:hover .products-list-item_blur {
        background: #000;
        position: absolute;
        top: 0;
        width: 258px;
        height: 110%;
        z-index: 2;
        opacity: 0.05;
        margin: -11px;
        display: none;
    }

    .product-list-item__badges {
        position: relative;
        top: 324px;
    }
</style>
