async function search() {
  const email = document.getElementById("email").value;
  const res = await fetch(`/search?email=${email}`);
  const data = await res.json();

  document.getElementById("phone").value = data.phone;
  document.getElementById("org").value = data.organization;
}

async function update() {
  await fetch("/update", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      email: email.value,
      phone: phone.value,
      organization: org.value
    })
  });
  alert("Updated!");
}
