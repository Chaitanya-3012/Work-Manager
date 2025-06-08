import { useState } from "react";

export default function Service() {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    try {
      const response = await fetch("http://localhost:8000/item");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error("Fetch error:", error);
    }
  };
  return (
    <div>
      <h1>Hello</h1>
      <button onClick={fetchData}>Fetch Data</button>
      {data.map((item, index) => (
        <div key={index}>
            <h2>{item.name}</h2>
            <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}
