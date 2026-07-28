<?php
$botToken = "8715161032:AAHvKtpd6Q_FbhNe38F_7o1WIcTk51xp-Zw";
$chatId = "261458452";

$name = $_POST['name'] ?? 'Не указано';
$phone = $_POST['phone'] ?? 'Не указано';
$message = $_POST['message'] ?? 'Без сообщения';

$text = "🪑 *Новая заявка с Mero!*\n\n";
$text .= "👤 *Имя:* $name\n";
$text .= "📞 *Телефон:* $phone\n";
$text .= "💬 *Сообщение:* $message";

$url = "https://api.telegram.org/bot$botToken/sendMessage";
$data = [
    'chat_id' => $chatId,
    'text' => $text,
    'parse_mode' => 'Markdown'
];

$options = [
    'http' => [
        'method' => 'POST',
        'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
        'content' => http_build_query($data)
    ]
];

$context = stream_context_create($options);
$result = file_get_contents($url, false, $context);

header('Location: index.html#catalog');
echo "<script>alert('Спасибо! Мы свяжемся с вами в ближайшее время.'); window.location.href='index.html';</script>";
?>