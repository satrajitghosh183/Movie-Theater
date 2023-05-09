import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [movieCID, setMovieCID] = useState('');
  const [ticketID, setTicketID] = useState('');
  const [paymentIntentID, setPaymentIntentID] = useState('');

  const handleMovieUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('movie', file);

    try {
      const response = await axios.post('/upload-movie', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setMovieCID(response.data.cid);
    } catch (error) {
      console.error(error);
    }
  };

  const handleTicketPurchase = async () => {
    try {
      const response = await axios.post('/purchase-ticket', {
        movieCID: movieCID
      });
      setTicketID(response.data.ticketID);
      setPaymentIntentID(response.data.paymentIntentID);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Movie Upload</h1>
      <input type="file" accept=".mp4" onChange={handleMovieUpload} />

      {movieCID && (
        <div>
          <h2>Movie CID: {movieCID}</h2>
          <button onClick={handleTicketPurchase}>Purchase Ticket</button>
        </div>
      )}

      {ticketID && (
        <div>
          <h2>Ticket ID: {ticketID}</h2>
          <h2>Payment Intent ID: {paymentIntentID}</h2>
        </div>
      )}
    </div>
  );
}

export default App;
