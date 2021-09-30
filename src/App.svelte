<script>
	let name = "world";
	let visible = false;
	function handleMouseOver() {
		visible = true;
	}
	function handleMouseOut(e) {
		visible = false;
	}
</script>

<!-- <h1>Hello {name}!</h1> -->
<div
	class="products-list-item"
	data-sku="MP002XM1RK04"
	data-quick-promotion-provider-id=""
	data-position="2"
	data-src="./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg"
	data-type="category"
	data-block=""
	data-rollover="./img236x341/M/P/MP002XM1RK04_15191679_2_v1_2x.jpg"
	data-gallery="[./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg , ./img236x341/M/P/MP002XM1RK04_15191679_2_v1_2x.jpg , ./img236x341/M/P/MP002XM1RK04_15191680_3_v1_2x.jpg , ./img236x341/M/P/MP002XM1RK04_15191681_4_v1_2x.jpg]"
	data-price="1599"
	on:mouseenter={handleMouseOver}
	on:mouseleave={handleMouseOut}
>
	<a
		href="/p/mp002xm1rk04/clothes-zolla-pulover/"
		data-sku="MP002XM1RK04"
		data-position="2"
		class="products-list-item__link link"
	>
		<div class="product-list-item__gallery">
			<div class="product-list-item__gallery-page" data-id="0" />
			<div class="product-list-item__gallery-page" data-id="1" />
			<div class="product-list-item__gallery-page" data-id="2" />
			<div class="product-list-item__gallery-page" data-id="3" />
		</div>
		<div
			class="to-favorites js-to-favorites                      to-favorites_wish-groups"
			data-sku="MP002XM1RK04"
			data-image="./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg"
			data-price-origin="1599"
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
				class="products-list-item__img"
				width="236"
				height="341"
				src="./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg"
				alt="Пуловер, Zolla, цвет: коричневый. Артикул: MP002XM1RK04. Одежда / Джемперы, свитеры и кардиганы"
			/>

			<span class="vue-widget product-list-item__badges">
				<!---->
			</span>
		</div>
		<span class="price"
			><span class="price__actual">1 599</span><span
				class="price__currency"
			>
				₽</span
			></span
		>
		<div class="products-list-item__brand">
			Zolla
			<span class="products-list-item__type"> Пуловер </span>
		</div>
	</a>
	<div class="groups-by-sku groups-by-sku_hidden" />
	<div class="products-list-item_blur" />
	{#if visible == true}
		<div class="products-list-item__extra">
			<div class="products-list-item__extra-info">
				<div class="products-list-item__sizes">
					<span class="products-list-item__sizes-title">
						Размеры (RUS):
					</span><a
						class="products-list-item__size-item link"
						href="/p/mp002xm1rk04/clothes-zolla-pulover/?sku=MP002XM1RK04"
						>46/48</a
					><a
						class="products-list-item__size-item link"
						href="/p/mp002xm1rk04/clothes-zolla-pulover/?sku=MP002XM1RK04"
						>48/50</a
					><a
						class="products-list-item__size-item link"
						href="/p/mp002xm1rk04/clothes-zolla-pulover/?sku=MP002XM1RK04"
						>50/52</a
					><a
						class="products-list-item__size-item link"
						href="/p/mp002xm1rk04/clothes-zolla-pulover/?sku=MP002XM1RK04"
						>52/54</a
					><a
						class="products-list-item__size-item link"
						href="/p/mp002xm1rk04/clothes-zolla-pulover/?sku=MP002XM1RK04"
						>54/56</a
					>
				</div>
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
	.products-list-item_hidden {
		display: none;
	}

	.products-list-grid_item {
		display: inline-block;
	}

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

	.products-list-item .price_denomination {
		font-size: 10px;
		line-height: 18px;
		color: #888;
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

	.products-list-item__button {
		background-color: #e9f4ff;
		color: #2796ff;
		border: 1px solid #e9f4ff;
		margin-bottom: 8px;
		margin-top: 10px;
		display: block;
		text-align: center;
	}

	.products-list-item__button.size-chooser-widget_active,
	.products-list-item__button:active,
	.products-list-item__button:focus,
	.products-list-item__button:hover {
		background-color: #cae5ff;
		color: #0060d2;
		border: 1px solid #cae5ff;
	}

	.products-list-item__button_out-of-stock,
	.products-list-item__button_out-of-stock:active,
	.products-list-item__button_out-of-stock:focus,
	.products-list-item__button_out-of-stock:hover {
		color: #888;
		border-color: #e5e5e5;
		background: #e5e5e5;
		cursor: default;
	}

	.products-list-item_mp_label {
		font-weight: 500;
		padding: 0 10px;
		letter-spacing: 0.1px;
		border-radius: 8px;
		font-size: 10px;
		line-height: 16px;
		color: #fff;
		text-transform: uppercase;
		margin-top: 5px;
		display: none;
	}

	.products-list-item_mp_label-red .products-list-item_mp_label {
		background-color: #f93c00;
		display: inline-block;
	}

	.products-list-item_mp_label-green .products-list-item_mp_label {
		background-color: #00a200;
		display: inline-block;
	}

	.products-list-item_mp_label-grey .products-list-item_mp_label {
		background-color: #888;
		display: inline-block;
	}

	.products-list-item__cd {
		color: #f93c00;
		padding-top: 7px;
		height: 20px;
	}

	.products-list-item__cd-digits {
		display: inline-block;
		padding-right: 10px;
		margin-right: 10px;
	}

	.products-list-item__img-wrapper {
		position: relative;
	}

	.products-list-item .product-label-UI10997 {
		display: none;
		bottom: 28px;
	}

	.not-touch .products-list-item:hover .product-label-UI10997 {
		display: inline-block;
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

	.products-list-item_adv-sku > a,
	.products-list-item_adv-sku > a > img {
		display: block;
	}

	.products-list-item_adv-sku > a > img {
		width: 100%;
	}

	.products-list-item_adv-middle {
		position: relative;
		display: block;
		width: auto;
	}

	.products-catalog_wishlist .product-list-item__gallery {
		display: none;
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

	.t-products-sis .product-list-item__badges {
		position: absolute;
		top: 260px;
		margin: -16px 0 0;
	}
</style>
