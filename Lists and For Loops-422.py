## 1. Lists ##

row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
print(row_2)
print(row_3)

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1 = row_1[3]
print(ratings_1)
ratings_2 = row_2[3]
ratings_3 = row_3[3]
total = ratings_1 + ratings_2 + ratings_3
average = total / 3
print(average)

## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[-1]
print(rating_1)

rating_2 = row_2[-1]
print(rating_2)

rating_3 = row_3[-1]
print(rating_3)

total_rating = rating_1 + rating_2 + rating_3
print(total_rating)

average_rating = total_rating / 3
print(average_rating)

## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0], row_1[3], row_1[4]]
print(fb_rating_data)

insta_rating_data = [row_2[0], row_2[3], row_2[4]]
print(insta_rating_data)

pandora_rating_data = [row_5[0], row_5[3], row_5[4]]
print(pandora_rating_data)

avg_rating = (fb_rating_data[2] + insta_rating_data[2] + pandora_rating_data[2]) / 3
print(avg_rating)

## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

first_4_fb = row_1[0:4]
print(first_4_fb)

last_3_fb = row_1[2:5]
print(last_3_fb)

pandora_3_4 = row_5[2:4]
print(pandora_3_4)

## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
print(app_data_set)

avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]) / 5
print(avg_rating)

## 7. Opening and Reading a File ##

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
print(read_file[:300])
opened_file.close()

## 8. From Strings to Lists ##

new_line_split = read_file.split("\n")
header_list = new_line_split[0].split(",")
row_1_list = new_line_split[1].split(",")
row_2_list = new_line_split[2].split(",")
first_three_lists = [header_list, row_1_list, row_2_list]