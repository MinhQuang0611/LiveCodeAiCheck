<?php
// Nhập số lượng môn học
$n = intval(trim(fgets(STDIN)));

// Nhập danh sách điểm
$scores = [];
$input = trim(fgets(STDIN));
$scores = array_map('floatval', explode(' ', $input));

// Tính điểm trung bình
$total = array_sum($scores);
$average = $total / $n;
$average = round($average, 2);

// Xếp loại học sinh
if ($average >= 8.5) {
    $rank = "Xuat sac";
} elseif ($average >= 7.0) {
    $rank = "Gioi";
} elseif ($average >= 5.5) {
    $rank = "Kha";
} elseif ($average >= 4.0) {
    $rank = "Trung binh";
} else {
    $rank = "Yeu";
}

// In kết quả
echo number_format($average, 2); echo "\n" . $rank . PHP_EOL;
?>
