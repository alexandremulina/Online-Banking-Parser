const banks = document.querySelectorAll(".bank-card");

banks.forEach((bank) => {
  const bankInfo = bank.querySelector(".bank-info");
  const apiResources = bank.querySelector(".api-resources");
  bankInfo.addEventListener("click", () => {
    bank.classList.toggle("bank-card-active");
    const status = bank.querySelector(".bank-status");
    status.style.display = status.style.display === "none" ? "" : "none";
    apiResources.classList.toggle("d-none");
    bankInfo.querySelector(".bank-name").classList.toggle("active");
    const arrow = bankInfo.querySelector("i");
    arrow.classList.toggle("fa-chevron-right");
    arrow.classList.toggle("fa-chevron-down");
    arrow.classList.toggle("active");
  });
});

const searchBank = () => {
  var inputValue = document.getElementById("search_query").value.toLowerCase();
  banks.forEach((bank) => {
    const name = bank.querySelector(".bank-name").innerText.toLowerCase();
    name.includes(inputValue)
      ? (bank.style.display = "block")
      : (bank.style.display = "none");
  });
};
