document.addEventListener("DOMContentLoaded", () => {
  const taskInput = document.getElementById("taskInput");
  const addTaskButton = document.getElementById("addTaskButton");
  const taskList = document.getElementById("taskList");

  addTaskButton.addEventListener("click", () => {
    const taskText = taskInput.value.trim();
    if (taskText) {
      const listItem = document.createElement("li");
      listItem.textContent = taskText;

      // Thêm chức năng tick hoàn thành
      listItem.addEventListener("click", function (e) {
        // Không toggle khi bấm vào nút Remove
        if (e.target === listItem) {
          listItem.classList.toggle("completed");
        }
      });

      const removeButton = document.createElement("button");
      removeButton.textContent = "Remove";
      removeButton.className = "remove-btn";
      removeButton.addEventListener("click", (e) => {
        e.stopPropagation(); // Không bị tick khi xóa
        taskList.removeChild(listItem);
      });

      listItem.appendChild(removeButton);
      taskList.appendChild(listItem);
      taskInput.value = "";
    }
  });
});
