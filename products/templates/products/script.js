document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const products = document.querySelectorAll(".product");

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const filterValue = button.dataset.filter;
      products.forEach((product) => {
        product.style.display = "none";
        if (product.classList.contains(filterValue) || filterValue === "all") {
          product.style.display = "block";
        }
      });
    });
  });
});