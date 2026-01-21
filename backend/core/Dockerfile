# --- Build stage ---
FROM eclipse-temurin:21-jdk AS build
WORKDIR /server

# First step is maven build cache only
COPY .mvn .mvn
COPY mvnw .
COPY pom.xml .

# Make wrapper executable and download dependencies only
RUN chmod +x ./mvnw && ./mvnw dependency:go-offline -B

# Next build from source
COPY src ./src
RUN ./mvnw clean package -DskipTests

# --- Run stage ---
FROM eclipse-temurin:21-jre AS run
WORKDIR /server

# Copy the earlier built jar file
COPY --from=build /server/target/*.jar ./journal-service.jar

# Port
EXPOSE 7075

# Run the application with optional memory limits
ENTRYPOINT ["java", "-Xms256m", "-Xmx512m", "-jar", "journal-service.jar"]
