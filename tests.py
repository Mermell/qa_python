from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

   

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_only_one_time(self):
        collect = BooksCollector()
        collect.add_new_book('Сильмариллион')
        collect.add_new_book('Сильмариллион')
        assert len(collect.get_books_genre()) == 1

    import pytest

    @pytest.mark.parametrize('genre, book_name', [('Ужасы', 'Сны Ктулху')])

    def test_set_book_genre_valid_genre(self, genre, book_name):
        genre_collector = BooksCollector()
        genre_collector.add_new_book(book_name)
        genre_collector.set_book_genre(book_name, genre)
        assert genre_collector.get_books_genre()[book_name] == genre

    @pytest.mark.parametrize('genre, book_name', [('Фэнтези', 'Сильмариллион')])
    def test_set_book_genre_genre_not_in_self_genre(self, genre, book_name):
        genre_collector = BooksCollector()
        genre_collector.add_new_book(book_name)
        genre_collector.set_book_genre(book_name, genre)
        assert genre_collector.get_books_genre()[book_name] == ''


    def test_get_book_genre_return_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Сильмариллион')
        assert collector.get_book_genre('Сильмариллион') == ''
         
    @pytest.mark.parametrize('genre, book_name', [('Ужасы', ['Сны Ктулху']), ('Мультфильмы', [])])
    
    def test_get_books_with_specific_genre_return_name_by_genre(self, genre, book_name):
        collector = BooksCollector()
        collector.add_new_book('Сны Ктулху')
        collector.set_book_genre('Сны Ктулху', 'Ужасы')
        result = collector.get_books_with_specific_genre(genre)
        assert result == book_name

    def test_get_books_genre_return_books_and_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Робин Гуд')
        collector.set_book_genre('Робин Гуд', 'Мультфильмы')
        collector.add_new_book('Сны Ктулху')
        collector.set_book_genre('Сны Ктулху', 'Ужасы')
        result = collector.get_books_genre()
        assert result == {'Робин Гуд':'Мультфильмы','Сны Ктулху':'Ужасы'}

    def test_get_books_for_children_dont_have_books_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Робин Гуд')
        collector.set_book_genre('Робин Гуд', 'Мультфильмы')
        collector.add_new_book('Сны Ктулху')
        collector.set_book_genre('Сны Ктулху', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Робин Гуд' in result 
        assert 'Сны Ктулху' not in result 

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сильмариллион')
        collector.add_book_in_favorites('Сильмариллион')
        assert collector.favorites == ['Сильмариллион']   

    def test_delete_book_from_favorites_delete_only_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сильмариллион')
        collector.add_book_in_favorites('Сильмариллион')
        collector.add_new_book('Сны Ктулху')
        collector.add_book_in_favorites('Сны Ктулху')
        collector.delete_book_from_favorites('Сны Ктулху')
        assert collector.favorites == ['Сильмариллион']   

    def test_get_list_of_favorites_books_get_all_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Сильмариллион')
        collector.add_book_in_favorites('Сильмариллион')
        collector.add_new_book('Сны Ктулху')
        collector.add_book_in_favorites('Сны Ктулху')
        result = collector.get_list_of_favorites_books()
        assert result == ['Сильмариллион','Сны Ктулху']