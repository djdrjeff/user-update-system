async function searchUser() {
    const email = document.getElementById("email").value;
  
    const res = await fetch(`${API_BASE}/search?email=${email}`);
    if (!res.ok) {
      alert("User not found");
      return;
    }
  
    const data = await res.json();
    document.getElementById("phone").value = data.phone;
    document.getElementById("organization").value = data.organization;
  }
  
  async function submitUpdate() {
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const organization = document.getElementById("organization").value;
  
    const res = await fetch(`${API_BASE}/update`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, phone, organization })
    });
  
    if (res.ok) {
      alert("Update submitted successfully");
    } else {
      alert("Update failed");
    }
  }
  