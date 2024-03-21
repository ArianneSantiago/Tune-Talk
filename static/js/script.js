const editButtons = document.getElementsByClassName("btn-edit");
// const reviewText = document.getElementById("reviewForm");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let review_Id = e.target.getAttribute("data-review_id");
        // console.log(`reviewContent${review_Id}`);
        let reviewContent = document.getElementById(`reviewContent${review_Id}`).innerText;
        reviewForm.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${review_Id}`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let review_id = e.target.getAttribute("data-review_id");
        deleteConfirm.href = `delete_review/${review_id}`;
        deleteModal.show()
    });
}