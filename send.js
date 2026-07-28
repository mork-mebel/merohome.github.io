document.getElementById('orderForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = this.querySelector('[name="name"]').value;
    const phone = this.querySelector('[name="phone"]').value;
    const message = this.querySelector('[name="message"]').value || 'Без сообщения';
    
    const botToken = "8715161032:AAFCUgcYLJbDGjjCk6DrE0cGmlQgVBa1D_8";
    const chatId = "261458452";
    
    const text = `🪑 *Новая заявка с Mero!*\n\n👤 *Имя:* ${name}\n📞 *Телефон:* ${phone}\n💬 *Сообщение:* ${message}`;
    
    fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            chat_id: chatId,
            text: text,
            parse_mode: 'Markdown'
        })
    })
    .then(() => {
        alert('Спасибо! Мы свяжемся с вами.');
        document.getElementById('modal').classList.remove('modal--open');
        this.reset();
    })
    .catch(() => {
        alert('Ошибка отправки. Позвоните нам по телефону.');
    });
});