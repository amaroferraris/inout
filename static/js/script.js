const taskForm = document.getElementById("task-form");
const openTaskFormBtn = document.getElementById("open-task-form-btn");
const inButton = document.getElementById("in-button");


openTaskFormBtn.addEventListener('click', () => taskForm.classList.toggle('hidden'))
inButton.addEventListener('click', () => alert('jeje'))