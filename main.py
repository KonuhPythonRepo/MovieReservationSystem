import datetime
import os

from dotenv import load_dotenv

from database.hall_repository import HallRepository
from database.movie_repository import MovieRepository
from database.showtime_repository import ShowTimesRepository
from database.ticket_repository import TicketRepository
from database.user_repository import UserRepository
from security.hasher import Hasher
from use_cases import CreateShowtimeUseCase
from use_cases import CreateHallUseCase
from use_cases.LoginUserUseCase import LoginUserUseCase
from use_cases.ticket.CreateTicketUseCase import CreateTicketUseCase

load_dotenv()

CONN_STRING = os.getenv("CONNECTION_STRING")

user = UserRepository(CONN_STRING)
hash_ = Hasher()
login = LoginUserUseCase(user, hash_)
movie = MovieRepository(CONN_STRING)
showtime = ShowTimesRepository(CONN_STRING)
hall = HallRepository(CONN_STRING)
ticket = TicketRepository(CONN_STRING)
us = CreateTicketUseCase(ticket)

seat = int(input("Введите номер места: "))
row = int(input("Введите номер ряда: "))
price = int(input("Введите цену: "))
user_id = int(input("Введите ваш user_id: "))
showtime_id = int(input("Введите номер сеанса: "))
us.execute(seat, row, price,user_id, showtime_id )