<script>
	import Product from "./Product.svelte";
	let external_json_data = [
		{
			link: "/p/mp002xm1rk04/clothes-zolla-pulover/",
			name: "Пуловер",
			sku: "MP002XM1RK04",
			price: 1599,
			brand: "Zolla",
			image_src: "./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg",
			image_urls: [
				"./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg",
				"./img236x341/M/P/MP002XM1RK04_15191679_2_v1_2x.jpg",
				"./img236x341/M/P/MP002XM1RK04_15191680_3_v1_2x.jpg",
				" ./img236x341/M/P/MP002XM1RK04_15191681_4_v1_2x.jpg",
			],
			sizes: ["46/48", "48/50", "50/52", "52/54", "54/56"],
			gender: "men",
			color_family: "коричневый",
			is_sport: false,
			is_premium: false,
			season: "5592:мульти",
			is_new: "false",
			category: "Джемперы, свитеры и кардиганы",
			position: 2,
		},
		{
			link: "/p/mp002xm1rk04/clothes-zolla-pulover/",
			name: "Пуловер",
			sku: "MP002XM1RK04",
			price: 1599,
			brand: "Zolla",
			image_src: "./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg",
			image_urls: [
				"./img236x341/M/P/MP002XM1RK04_15191678_1_v1_2x.jpg",
				"./img236x341/M/P/MP002XM1RK04_15191679_2_v1_2x.jpg",
				"./img236x341/M/P/MP002XM1RK04_15191680_3_v1_2x.jpg",
				" ./img236x341/M/P/MP002XM1RK04_15191681_4_v1_2x.jpg",
			],
			sizes: ["46/48", "48/50", "50/52", "52/54", "54/56"],
			gender: "men",
			color_family: "коричневый",
			is_sport: false,
			is_premium: false,
			season: "5592:мульти",
			is_new: "false",
			category: "Джемперы, свитеры и кардиганы",
			position: 2,
		},
	];
</script>

<Product json_data={external_json_data[0]} />
<Product json_data={external_json_data[1]} />
