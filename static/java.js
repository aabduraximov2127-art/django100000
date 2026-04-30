document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const inputs = document.querySelectorAll("input, textarea, select");
    const button = document.querySelector(".btn");

    // 🔵 Focus effect
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.parentElement.style.transform = "scale(1.02)";
        });

        input.addEventListener("blur", () => {
            input.parentElement.style.transform = "scale(1)";
        });
    });

    // 🔴 Validation
    form.addEventListener("submit", (e) => {
        let valid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                valid = false;
                input.style.border = "1px solid red";
            } else {
                input.style.border = "1px solid #ccc";
            }
        });

        if (!valid) {
            e.preventDefault();
            showToast("❌ Iltimos, barcha maydonlarni to‘ldiring!");
            return;
        }

        // 🟢 Loading effect
        button.innerText = "Loading...";
        button.disabled = true;
    });

    // 🟡 Toast function
    function showToast(message) {
        const toast = document.createElement("div");
        toast.innerText = message;
        toast.className = "toast";

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.add("show");
        }, 100);

        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
});

document.addEventListener("DOMContentLoaded", () => {

    // 🖼 Avatar click effect
    const avatar = document.querySelector(".profile-img img");

    if (avatar) {
        avatar.addEventListener("click", () => {
            avatar.classList.toggle("active");
        });
    }

    // 🎨 Button ripple effect
    const buttons = document.querySelectorAll(".btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", function (e) {
            const circle = document.createElement("span");
            circle.classList.add("ripple");

            const rect = this.getBoundingClientRect();
            circle.style.left = (e.clientX - rect.left) + "px";
            circle.style.top = (e.clientY - rect.top) + "px";

            this.appendChild(circle);

            setTimeout(() => {
                circle.remove();
            }, 600);
        });
    });

    // ⚠️ Delete confirm
    const deleteBtn = document.querySelector(".delete");

    if (deleteBtn) {
        deleteBtn.addEventListener("click", (e) => {
            if (!confirm("Rostdan ham o‘chirmoqchimisiz?")) {
                e.preventDefault();
            }
        });
    }

});

document.addEventListener("DOMContentLoaded", () => {
    const deleteBtn = document.querySelector(".danger");

    if (deleteBtn) {
        deleteBtn.addEventListener("click", (e) => {
            if (!confirm("Aniq o‘chirasizmi? 😢")) {
                e.preventDefault();
            }
        });
    }
});