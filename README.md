# Python Flask CRUD Application

## This is Python Flask CRUD Application with backend database MYSQL. It covers all operation that is create, read, edit and delete

- Install Required Packaged (requirements.txt)
- Enter Database credentials in app.py line no. 12 - 15
- Database Patch Frist Apply below script in the database for table structure
1. create database crud;

2. use crud;

<!-- Table Structure  -->

3. CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

 <!-- Dumping dummy data for table `students` -->

4. INSERT INTO `students` (`id`, `name`, `email`, `phone`) VALUES
(1, 'Somnath Mugdal', 'soma@gmail.com', '9137023840'),
(2, 'Pratap Zende', 'pzende@gmail.com', '7878989800'),
(3, 'Pooja Tike', 'poojatike@gmail.com', '9876543210'),
(4, 'Ajay Mane', 'ajaymane@gmail.com', '9977885462');

5. ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

 <!-- AUTO_INCREMENT for table `students` -->

6. ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

<!-- Commit the changes -->
7. COMMIT;

- To run the App use **python app.py**
- For any error or process check log file **crud.log**
