-- website_movie: test data
INSERT INTO website_movie VALUES(1, "The Hunger Games: Catching Fire", 7.9);
INSERT INTO website_movie VALUES(2, "Wreck-It Ralph", 7.8);
INSERT INTO website_movie VALUES(3, "Her", 8.3);
INSERT INTO website_movie VALUES(4, "American Sniper", 5.9);
INSERT INTO website_movie VALUES(5, "Hobbit 1", 8.2);
INSERT INTO website_movie VALUES(6, "Hobbit 2", 8.1);
INSERT INTO website_movie VALUES(7, "Hobbit 3", 8.0);
INSERT INTO website_movie VALUES(8, "Lord of the rings - I", 9.0);
INSERT INTO website_movie VALUES(9, "Lord of the rings - II", 9.4);
INSERT INTO website_movie VALUES(10, "Lord of the rings - III", 9.2);
INSERT INTO website_movie VALUES(11, "HIT MAN", 6.6);
INSERT INTO website_movie VALUES(12, "HIT MAN - Agent 47", 7.1);
INSERT INTO website_movie VALUES(13, "Fast and Furious", 6.9);

-- website_projection(id, movie_id, type, date, time, hall): test data
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(1, 1, 2, "2014-05-01", "19:00", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(2, 1, 1, "2015-05-01", "19:10", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(3, 1, 3, "2015-05-02", "21:10", 3);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(4, 3, 1, "2015-05-03", "20:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(5, 2, 2, "2015-05-02", "22:00", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(6, 2, 1, "2015-05-02", "14:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(7, 4, 1, "2015-05-03", "18:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(8, 4, 1, "2015-05-04", "21:00", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(9, 11, 1, "2015-05-04", "20:00", 4);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(10, 11, 1, "2015-05-04", "18:00", 5);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(11, 8, 1, "2015-05-06", "17:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(12, 8, 2, "2015-05-06", "19:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(13, 9, 1, "2015-05-07", "17:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(14, 9, 2, "2015-05-07", "18:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(15, 9, 2, "2015-05-07", "22:00", 4);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(16, 10, 2, "2015-05-08", "18:00", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(17, 10, 1, "2015-05-08", "19:00", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(18, 10, 2, "2015-05-08", "22:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(19, 13, 1, "2015-05-09", "15:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(20, 13, 2, "2015-05-10", "16:00", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(21, 13, 3, "2015-05-10", "19:30", 3);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(22, 13, 3, "2015-05-11", "20:00", 3);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(23, 3, 1, "2015-05-12", "15:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(24, 12, 1, "2015-06-20", "22:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(25, 12, 1, "2015-06-22", "20:30", 4);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(26, 5, 2, "2015-05-05", "20:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(27, 5, 1, "2015-05-05", "12:30", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(28, 5, 2, "2015-05-06", "20:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(29, 6, 2, "2015-05-15", "20:30", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(30, 6, 1, "2015-05-16", "16:00", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(31, 7, 1, "2015-05-18", "16:00", 1);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(32, 7, 2, "2015-05-19", "20:00", 2);
INSERT INTO website_projection(id, movie_id, type, date, time, hall) VALUES(33, 7, 2, "2015-05-21", "16:00", 2);
