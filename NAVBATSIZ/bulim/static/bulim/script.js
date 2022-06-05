const Navigation = () => {
  return /*#__PURE__*/(
    React.createElement("nav", { className: "nav--wrapper" }, /*#__PURE__*/
    React.createElement("div", { className: "nav--component" }, /*#__PURE__*/
    React.createElement("div", { className: "nav--item" }, /*#__PURE__*/
    React.createElement("a", { src: "#" }, "Logo"))), /*#__PURE__*/



    React.createElement("div", { className: "nav--component" }, /*#__PURE__*/
    React.createElement("div", { className: "nav--item" }, /*#__PURE__*/
    React.createElement("a", { href: "#" }, "Item 1")), /*#__PURE__*/

    React.createElement("div", { className: "nav--item" }, /*#__PURE__*/
    React.createElement("a", { href: "#" }, "Item 2")), /*#__PURE__*/

    React.createElement("div", { className: "nav--item" }, /*#__PURE__*/
    React.createElement("a", { href: "#" }, "Item 3")))));




};

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      items: [
      {
        product_id: 123124,
        product_name: "Notebook 9 Pro (256 GB)",
        image:
        "https://image-us.samsung.com/SamsungUS/home/computing/windows-laptops/pdp/np930mbe-k01us/930MBE_012_Dynamic1_Silver.jpg?$product-details-jpg$",
        price: "$1,099.99",
        about: "",
        rating: 4 },

      {
        product_id: 1222224,
        product_name: "Acer Aspire 5",
        image:
        "https://images-na.ssl-images-amazon.com/images/I/71sesDsw95L._AC_SL1500_.jpg",
        price: "$364.99",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 },

      {
        product_id: 12234,
        product_name: "Microsoft Surface Laptop Go ",
        image:
        "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6428/6428991_sd.jpg",
        price: "$699.00 ",
        about: "",
        rating: 4.5 }] };



  }

  render() {
    return /*#__PURE__*/(
      React.createElement(React.Fragment, null, /*#__PURE__*/
      React.createElement(Navigation, null), /*#__PURE__*/
      React.createElement("section", null, /*#__PURE__*/
      React.createElement("header", null, /*#__PURE__*/
      React.createElement("h2", null, "Our Products")), /*#__PURE__*/

      React.createElement("main", null,
      this.state.items.map((item, index) => {
        return /*#__PURE__*/(
          React.createElement("section", { key: item.product_id, className: "product_card" }, /*#__PURE__*/
          React.createElement("img", { src: item.image }), /*#__PURE__*/
          React.createElement("section", { className: "product_card--info" }, /*#__PURE__*/
          React.createElement("h3", null, item.product_name), /*#__PURE__*/
          React.createElement("h5", null, item.rating, " out of 5"), /*#__PURE__*/
          React.createElement("h4", null, item.price))));



      })))));




  }}


ReactDOM.render( /*#__PURE__*/React.createElement(App, null), document.getElementById("root"));