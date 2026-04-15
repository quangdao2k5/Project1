Mô tả các file
1. config.py
Chứa tất cả các hằng số và cấu hình:

Kích thước màn hình
FPS
Tốc độ
Vị trí ban đầu
Màu sắc

2. game_state.py
Class GameState quản lý toàn bộ trạng thái game:

Vị trí player và ghost
Điểm số, mạng
Trạng thái powerup
Phương thức reset game

3. assets.py
Load và quản lý tất cả hình ảnh game

4. map.py
Vẽ bản đồ với các loại tile khác nhau:

Chấm nhỏ (1)
Power pellet (2)
Tường các loại (3-8)
Cổng ghost (9)

5. player.py
Xử lý logic player:

Vẽ player với animation
Kiểm tra hướng có thể đi
Di chuyển player
Va chạm với chấm

6. ghost.py
Class Ghost với các phương thức:

draw(): Vẽ ghost
check_collisions(): Kiểm tra va chạm với tường
move_blinky(), move_inky(), move_pinky(), move_clyde(): Các kiểu di chuyển khác nhau

BLINKY(ĐỎ) : LÌ CẢ NGANG CẢ DỌC
PINKY(HỒNG) : LÌ KHI ĐI NGANG
INKY(XANH) : LÌ KHI ĐI DỌC
CLYDE(CAM) : ƯU TIÊN BẺ HƯỚNG TRÁI VÀ XUỐNG

7. ghost_ai.py
Tính toán target cho mỗi ghost:

Chế độ bình thường: 
BLINKY(ĐỎ) : TARGET PLAYER
PINKY(HỒNG) : TARGET Ô CÁCH 4 TRƯỚC MẶT PLAYER
INKY(XANH) : TARGET VỊ TRÍ ĐỐI XỨNG VỚI BLINKY THÔNG QUA 2 Ô TRƯỚC MẶT PLAYER
CLYDE(CAM) : CÁCH > 8 Ô THÌ ĐUỔI NHƯ BLINKY CÒN KHÔNG THÌ CHẠY VỀ GÓC

Chế độ powerup: chạy trốn
Chế độ đã bị ăn: về box

8. collision.py
Xử lý va chạm:

Player vs Ghost (mất mạng)
Player vs Ghost khi powerup (ăn ghost)
Hồi sinh ghost

9. ui.py
Vẽ giao diện người dùng:

Điểm số
Số mạng
Trạng thái powerup
Thông báo game over/victory

10. main.py
File chính kết nối tất cả:

Khởi tạo game
Game loop
Xử lý input
Cập nhật và vẽ

